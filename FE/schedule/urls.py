from django.urls import path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.scheduleList, name='schedulelist'),
    path('create/', views.scheduleCreate, name='schedulecreate'),
    path('schedule/<int:pk>/', views.scheduleDetail, name='scheduledetail'),
    path('schedule/<int:pk>/update/', views.scheduleUpdate, name='scheduleupdate'),
]
