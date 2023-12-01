# Custom User Model
## How to
### models.py에 AbstractUser를 상속하여 만든다.
```python
# models.py
from djang.db ipmort models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	...
```
`AbstractBaseUser` 를 상속하는 방법도 있지만, 
해당 클래스를 상속하면 따로 구현해야할 사항이 많아진다.

* `USERNAME_FIELD`: username으로 사용할 field를 설정한다.
* `REQUIRED_FIELDS`: custom user model에 필수적으로 입력해야 할 field를 설정한다.
* `objects = CustomUserManager()`: custom user model을 관리하는 manager class를 설정한다.

## DRF에서 pk를 설정하는 방법
### how to
#### `lookup_field`를 사용한다.
`APIView` 를 상속받는 class에서 원하는 필드를 다루려고 할 때,
`lookup_field` 에 field를 설정하여 사용한다.
* 기본값: `lookup_field = 'pk'`
* 변경값: `lookup_field = 'username'`  -- username으로 field 변경

## CORS(Cross-Origin Resource Sharing) 처리
"자신의 Origin과 다른 Origin에 대한 요청(교차 출처)의 자원을 공유할 것이냐"
local에서도 Port number가 다르면 서로 다른 출처(Origin)으로 본다.
브라우저는 기본적으로 SOP(Same Origin Policy) 정책 

`settings.py`에서,

`INSTALLED_APPS`에 `'corsheaders'` 추가,

`MIDDLEWARE`에 `'corsheaders.middleware.CorsMiddleware'` 추가,

허용할 url을 `CORS_ALLOWED_ORIGINS=[]`리스트에 url을 입력해서 허용할 출처(Origin)를 등록한다.

## JavaScript를 통해 API response 받기
```javascript
const url = "http://{{FRONT_END_URL}}/account/login/";
const $username = document.getElementById("username");
const $password = document.getElementById("password");
const $loginForm = document.querySelector("#login-form");

$loginForm.addEventListener("submit", (e) => {
	e.preventDefault();
	login();
});

async function login() {
	fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username: $username.value,
			password: $password.value,
		}),
	})
		.then((res) => res.json())
		.then((data) => {
			for (const key in data) {
				localStorage.setItem(key, data[key]);
			}
		})
		.catch((error) => {
			alert(error);
		});
}
```

## forms.py 를 통해 FormView로 form 다루기
* forms.py
```python
from django import forms
  
class LoginForm(forms.Form):
    username = forms.CharField(max_length=24, label='아이디')
    password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
```

## Front End: \<JavaScript\> Form data 전송 후, Response 저장, 이후 Redirect
### 1. Form data 전송
```JavaScript
const url = "http://{{BACK_END_URL}}/account/login/"; 
// form data를 전송할 URL

const $loginForm = document.querySelector("form");
const $username = document.getElementById("username");
const $password = document.getElementById("password");

$loginForm.addEventListener("submit", async (e) => {
	e.preventDefault();
	const response = await fetch(url, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username: $username.value,
			password: $password.value,
		}),
	});
```
### 2. 200 response 받은 후, localstorage에 저장, redirect
```JavaScript
...이어서
if (response.ok) {
            const data = await response.json();
            for (const key in data) {
                localStorage.setItem(key, data[key]);
            }
            window.location.href = "http://" + location.host;
        }
    });
```

## drf custum user model
[[D.R.F] 커스텀 유저 구현하기 - 회원가입, 로그인 (tistory.com)](https://wisdom-990629.tistory.com/entry/DRF-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%9C%A0%EC%A0%80-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EB%A1%9C%EA%B7%B8%EC%9D%B8)
[[DRF] dj_rest_auth로 커스텀 회원가입 구현하기 (velog.io)](https://velog.io/@ready2start/DRF-djrestauth%EB%A1%9C-%EC%BB%A4%EC%8A%A4%ED%85%80-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
## Custom user model 비밀번호 확인
### models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
  

class CustomUser(AbstractUser):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] # email을 필수로 받음
    objects = CustomUserManager()
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.username
```
### serializers.py
```python
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    verify_password = serializers.CharField(label='비밀번호 확인')
    # serializer에 verify_password를 생성하고, field에 등록한다.

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'verify_password']
  

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
```
먼저 `'verfy_password'`변수를 생성하고, `fields`에 등록한다.
그렇게 하지 않으면, 원래 모델의 없는 `'verfy_password'`를 추가해서 에러가 발생하고,
signup 페이지에서 해당 비밀번호 확인 폼이 나타나지 않는다.


## 최초 실행시 흐름
1. `serializer`: `class Meta`
2. `views`: `class view` 
3. \<action 발생\>
4. 해당 `view`의 `serializer` 메소드 실행
5. 해당 `serializer`의 연결된 `model`의 `manage` 실행

## SignUp error message custom하기
### 무식한 방법으로...
`RegisterSerializer`를 상속하여 `CustumSignUp Serializer`를 생성했다.

```python
class CustomRegisterSerializer(RegisterSerializer):
	pass
```
validate 메시지를 바꾸고 싶었고, 
```python
class CustomRegisterSerializer(RegisterSerializer):

    def validate_username(self, username):
        if get_user_model().objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("이미 사용중인 아이디입니다.")
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError("이미 사용중인 이메일입니다.")
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return data
```
상속받은 `RegisterSerializer`에서 해당 메시지를 띄우는 validate를 찾아, ValidationError를 띄우는 메시지를 수정했다.
user validation은 존재하지 않아, 직접 추가하였다.


## Custom user creation에서 "ConnectionRefusedError: [WinError 10061] 대상 컴퓨터에서 연결을 거부했으므로 연결하지 못했습니다" 문제

* Email 인증 모듈에서 발생한 문제
* Email을 인증 받는 settings.py 기본 설정이 켜져 있었다.
	* 	settings.py에 `ACCOUNT_EMAIL_VERIFICATION='none'` 을 추가한다.
		*  `ACCOUNT_EMAIL_VERIFICATION='none'`: 이메일 인증을 받아야지 계정 사용가능
		* `ACCOUNT_EMAIL_VERIFICATION='medatory'`: 이메일 인증을 받지 않으면 계정을 사용할 수없음
		* `ACCOUNT_EMAIL_VERIFICATION='optional'`: 가입 완료 인증 이메일은 발송되지만, 계정 사용가능
	* 나의 프로젝트의 경우에선, 인증 이메일을 보내는 기능이 없기 때문에 문제를 계속해서 보냈다.
## Viewset에서 Foreignkey 접근
### model.py
```python
class Post(models.Model):
    author = models.ForeignKey(
        "accounts.CustomUser", verbose_name="author", on_delete=models.CASCADE, related_name='author')
```
`ForeingKey`의 `related_name`을 통해 연결,

### serializers.py
```python
class CustomPostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ['author', 'title', 'created_at',
                  'updated_at', 'schedule', 'content']
```
해당 `related_name`을 `StringRelatedField`로 `serializers`에 받도록 한다.
`StringRelatedField`는 해당 `ForeingKey`의 `__str__` 메소드를 받는다.
