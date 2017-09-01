# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # redirect해도 로그아웃 되는걸 막기 위함

# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = "HWI HAN"

    args = {'myName':name, 'numbers':numbers}
    return render(request, 'accounts/home.html', args)
    #return render(request, 'accounts/login.html', args)   #HttpResponse('Home page!')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # 유저 생성해서 DB에 넣음
            return redirect('/account')
    else: #GET일 경우
        form = RegistrationForm()

        args ={'form':form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user) #UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else: # Get
        form = EditProfileForm(instance=request.user) #UserChangeForm(instance=request.user)
        args ={'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else: # Get
        form = PasswordChangeForm(user=request.user)
        args ={'form': form}
        return render(request, 'accounts/change_password.html', args)
