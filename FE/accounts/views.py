from typing import Any
from django.shortcuts import render
from django.conf import settings
from django.views.generic import FormView
from . import forms
from django.http import HttpRequest, request


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['BACK_END_URL'] = settings.BACK_END_URL
        return context

    def form_valid(self, form):
        # self.request.session['user'] = form.email
        return super().form_valid(form)


# def login(request):
#     context = {
#         'BACK_END_URL': settings.BACK_END_URL,
#     }
#     return render(request, 'accounts/login.html', context=context)


def signup(request):
    context = {
        'BACK_END_URL': settings.BACK_END_URL,
    }
    return render(request, 'accounts/signup.html', context=context)


login = LoginView.as_view()
