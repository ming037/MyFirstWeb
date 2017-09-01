# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm): # inherit
    email = forms.EmailField(required=True)

    class Meta: # contain Metadata
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
         )
    def save(self, commit=True): # override
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save() #sql database saving
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password') #포함하고 싶은 필드, password는 꼭 포함하여야 한다.
        exclude = () #제거하고 싶은 필드 , 둘 중 아무거나 사용해도 상관없음
