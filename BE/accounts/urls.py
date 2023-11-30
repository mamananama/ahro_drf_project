from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('api', views.ProfileViewSet)
# router.register('signup', views.ProfileViewSet)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('userinfo/', views.get_user_info, name='userinfo'),
    path('', include(router.urls)),
]
