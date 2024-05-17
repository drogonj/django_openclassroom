from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from . import forms

# def login_page(request):
#     form = forms.LoginForm()
#     message = ''
#     if (request.method == 'POST'):
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 message = 'Identifiants invalides.'
#     return render(request, 'authentification/login.html',
#                   {'form': form, 'message': message})

# setting Login Page View to class instead of a function

# class LoginPageView(View):
#     template_name = 'authentification/login.html'
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context=
#         {'form':form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Identifiants invalides.'
#         return render(request, self.template_name, context=
#             {'form': form, 'message': message})

# Who needs it anyway ? Django have a class named LoginView that do the work for us (see urls.py)

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html',
                  {'form': form})

def logout_page(request):
    logout(request)
    return redirect('login')

def upload_profile_picture(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentification/upload_profile_picture.html', context={'form': form})
