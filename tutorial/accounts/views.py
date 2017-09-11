# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse # url 하드코딩 없애기 위해서 사용
from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # redirect해도 로그아웃 되는걸 막기 위함
from django.contrib.auth.decorators import login_required # 로그인 하지 않은 상태에서 페이지에 접근 못하게 하기 위함

# Create your views here.
'''
def home(request):
    numbers = [1,2,3,4,5]
    name = "HWI HAN"

    args = {'myName':name, 'numbers':numbers}
    return render(request, 'accounts/home.html', args)
    #return render(request, 'accounts/login.html', args)   #HttpResponse('Home page!')
'''
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # 유저 생성해서 DB에 넣음
            return redirect(reverse('accounts:home'))#redirect('/account')
    else: #GET일 경우
        form = RegistrationForm()

        args ={'form':form}
        return render(request, 'accounts/reg_form.html', args)

#@login_required   #decorator 기능, 로그인 하지 않으면 404에러 띄움
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user= request.user
    args = {'user':user}
    return render(request, 'accounts/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user) #UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))  # redirect('/account/profile')
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
            return  redirect(reverse('view_profile')) # redirect('/account/profile')
        else:
            return  redirect(reverse('accounts:change_password')) #redirect('/account/change-password')
    else: # Get
        form = PasswordChangeForm(user=request.user)
        args ={'form': form}
        return render(request, 'accounts/change_password.html', args)
