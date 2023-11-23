# Custom User Model
## How to
### step 1. models.py에 AbstractUser를 상속하여 만든다.
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

Django에서는 허용할 url을 `setting.py`에,
`CORS_ALLOWED_ORIGINS=[]`리스트에 url을 입력해서 허용할 출처(Origin)를 등록한다.

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
