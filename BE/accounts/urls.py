from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
# router.register('signup', views.ProfileViewSet)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('join/', include("dj_rest_auth.registration.urls")),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('', include(router.urls)),
]
