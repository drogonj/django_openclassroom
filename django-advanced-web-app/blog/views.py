from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

# @login_required
# def home(request):
#     return render(request, 'blog/home.html')

#making view in a class instead of a function

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'blog/home.html')
