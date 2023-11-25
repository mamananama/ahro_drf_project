from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('아이디가 입력되지 않았습니다.')
        if not email:
            raise ValueError('이메일이 입력되지 않았습니다.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
