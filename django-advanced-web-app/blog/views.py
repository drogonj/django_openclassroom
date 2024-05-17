from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View
from . import forms, models

# @login_required
# def home(request):
#     return render(request, 'blog/home.html')

#making view in a class instead of a function

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        photos = models.Photo.objects.all()
        return render(request, 'blog/home.html',
                      {'photos': photos})

@login_required
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo/photo_upload.html', context={'form': form})