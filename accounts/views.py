from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = "index.html"



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"

class LoginView(TemplateView):
    template_name = "accounts/login.html"
