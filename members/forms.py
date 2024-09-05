from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import bundleoptions
from .models import customer_details

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class bundleform(forms.ModelForm):
    class Meta:
        model=bundleoptions
        fields="__all__"
        exclude=['price']

class customer(forms.ModelForm):
    class Meta:
        model=customer_details
        fields="__all__"
        exclude=['username', 'price']
