from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name:
            raise forms.ValidationError("Name is required")

        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        print=int(price)
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0")

        return price

    def clean_stock(self):
        stock = self.cleaned_data['stock']

        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative")

        return stock