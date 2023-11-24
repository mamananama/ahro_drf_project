from typing import Any
from django.shortcuts import render
from django.conf import settings
from django.views.generic import FormView
from . import forms
from django.http import HttpRequest, request


class LoginView(FormView):
    template_name = 'accounts/account_form.html'
    form_class = forms.LoginForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['context_url'] = 'http://' + \
            settings.BACK_END_URL + '/account/login/'

        return context

    def form_valid(self, form):
        # self.request.session['user'] = form.email
        return super().form_valid(form)


# def login(request):
#     context = {
#         'BACK_END_URL': settings.BACK_END_URL,
#     }
#     return render(request, 'accounts/login.html', context=context)


class SignUpView(FormView):
    template_name = 'accounts/account_form.html'
    form_class = forms.SignupForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['context_url'] = 'http://' + \
            settings.BACK_END_URL + '/account/join/'
        return context

    def form_valid(self, form):
        return super().form_valid(form)


login = LoginView.as_view()
signup = SignUpView.as_view()
