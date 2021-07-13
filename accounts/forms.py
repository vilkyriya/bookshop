from django.contrib.auth.models import User
from shop.models import Order, Address, Payment
from django import forms


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", required=False)
    last_name = forms.CharField(label="Фамилия", required=False)
    email = forms.EmailField(label="E-mail", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CheckoutUpdateForm(forms.ModelForm):
    id_address = forms.ModelChoiceField(label="Адрес", widget=forms.RadioSelect, queryset=Address.objects.all())
    id_payment = forms.ModelChoiceField(label="Способ оплаты", widget=forms.RadioSelect, queryset=Payment.objects.all())

    class Meta:
        model = Order
        fields = ['id_address', 'id_payment']

