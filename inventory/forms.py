from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control custom-input-box',
            'placeholder': 'Enter stock name'
        })
        self.fields['brand'].widget.attrs.update({
            'class': 'form-control custom-input-box',
            'placeholder': 'Enter brand name'
        })
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control custom-input-box',
            'placeholder': 'Enter quantity',
            'min': '0'
        })
    class Meta:
        model = Stock
        fields = ['name','brand','quantity']