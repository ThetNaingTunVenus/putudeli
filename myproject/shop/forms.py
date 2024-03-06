from django import forms
from .models import *
from django.forms import inlineformset_factory

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ['shopname', 'phone', 'shop_address']
        widgets = {
            
            'shopname' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'shop_address' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class PickupItemsForm(forms.ModelForm):
    class Meta:
        model = PickupItems
        fields = ['customer_name', 'phone', 'address', 'invoice_amount']
        widgets = {
            'customer_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'phone' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_amount' : forms.NumberInput(attrs={'class': 'form-control'}),
        }


PickupInlineForm = inlineformset_factory(
    PickupRequest, PickupItems, form=PickupItemsForm,
    extra=1, can_delete=True,
    can_delete_extra=True
)
