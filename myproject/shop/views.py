import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,UpdateView
from django.contrib import messages
from .forms import *
from .models import *

from account.views import *

class ShopHome(View):
    def get(self, request):
        return render(request, 'shop/ShopHome.html')

class PickupRequestView(View):
    def get(self, request):
        pr = PickupRequest.objects.filter(usr=request.user)
        pt = PickupItems.objects.filter(shop_usr=request.user)
        context = {'pr': pt}
        return render(request, 'shop/PickupRequestView.html', context)

class PickupRequestInline():
    form_class = PickupRequestForm
    model = PickupRequest
    template_name = "shop/pk_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))
        usr = self.request.user
        form.instance.usr = usr
        # print(usr)
        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('shop:PickupRequestView')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # variants.usr = self.request.user
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.pickup = self.object
            variant.shop_usr = self.request.user
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this, if you have can_delete=True parameter set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.employee_name = self.object
            image.save()

class PickupCreate(PickupRequestInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(PickupCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': PickupInlineForm(prefix='variants'),
                # 'images': ImageFormSet(prefix='images'),
            }
        else:
            return {
                'variants': PickupInlineForm(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                # 'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

class PickupUpdate(PickupRequestInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(PickupUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': PickupInlineForm(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            # 'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }


def delete_variant(request, pk):
    try:
        variant = PickupItems.objects.get(id=pk)
    except PickupItems.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('shop:update_product', pk=variant.pickup.id)

    variant.delete()
    messages.success(
            request, 'Variant deleted successfully'
            )
    return redirect('shop:update_product', pk=variant.pickup.id)


