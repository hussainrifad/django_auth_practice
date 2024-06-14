from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
            messages.success(request, 'User Created Successfully')
            return redirect('home')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request=request, user=user)
                messages.success(request, 'User Logged in Successfully')
                return redirect('editprofile')
            else:
                messages.success(request, 'Incorrect Username or Password')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required
def editUserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.EditProfileForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print(form.cleaned_data)
                messages.success(request, 'User Edited Successfully')
                return redirect('home')
        else:
            form = forms.EditProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('userlogin')

@login_required
def changeUserPassword(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(user=request.user, data = request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                update_session_auth_hash(request=request, user=form.user)
                messages.success(request, 'Password Updated Successfully')
                return redirect('home')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passwordchange.html', {'form':form})
    else:
        return redirect('userlogin')

@login_required
def changeUserPassword2(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(user=request.user, data = request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                update_session_auth_hash(request=request, user=form.user)
                messages.success(request, 'Password has Changed Successfully')
                return redirect('home')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passwordchange2.html', {'form': form})
    else:
        return redirect('userlogin')

@login_required
def userLogOut(request):
    if request.user is not None:
        logout(request)
        messages.success(request, 'User Logout Successfully')
        return redirect('userlogin')