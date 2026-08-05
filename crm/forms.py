from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField

class OrderForm(forms.ModelForm):
    order_phone=PhoneNumberField(region='AZ',error_messages={'invalid': 'Please enter a valid phone number.'}, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number','id':'phone'}))
    order_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    order_desc=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter your description'}), required=False)


    class Meta:
        model = Order
        fields = ['order_name', 'order_phone','order_desc']