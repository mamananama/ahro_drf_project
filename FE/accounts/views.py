from typing import Any
from django.shortcuts import render
from django.conf import settings
from django.views.generic import FormView
from . import forms


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def form_valid(self, form):
        # self.request.session['user'] = form.email
        return super().form_valid(form)


class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = forms.SignupForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context

    def form_valid(self, form):
        return super().form_valid(form)


def profile(request):
    print(f'request =========== {request.headers}')
    return render(request, 'main/index.html')


login = LoginView.as_view()
signup = SignUpView.as_view()
