from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, label='아이디', widget=forms.TextInput(
        attrs={'id': "username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': "password"}), label='비밀번호')


class SignupForm(forms.Form):
    username = forms.CharField(max_length=24, label='아이디')
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
    password2 = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')
