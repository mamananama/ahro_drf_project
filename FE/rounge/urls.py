from django.urls import path
from . import views

app_name = 'rounge'

urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('create/', views.postcreate, name='postcreate'),
    path('post/<int:pk>/', views.postdetail, name='postdetail'),
    path('post/<int:pk>/update/', views.postupdate, name='postupdate'),
]
