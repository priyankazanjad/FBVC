from django import forms
from .models import Laptop

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'company':'Enter Company Name',
            'model_name':'Enter Laptop Model Name',
            'ram':'Enter RAM',
            'rom':'Enter ROM',
            'processor':'Enter Processor',
            'price':'Enter Price',
            'weight':'Enter Weight in kg'
        }
        widgets = {
            'ram':forms.TextInput(attrs={'placeholder':'in GB'}),
            'rom':forms.TextInput(attrs={'placeholder':'in GB'})
        }

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram <= 0:
            raise forms.ValidationError('RAM must be grater than zero')
        elif ram % 2 != 0:
            raise forms.ValidationError('Enter valid RAM(even number)')
        else:
            return ram

    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom <= 0:
            raise forms.ValidationError('ROM must be grater than zero')
        else:
            return rom

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 10000:
            raise forms.ValidationError("Please enter valid Price")
        else:
            return price

