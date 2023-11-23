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