from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('accounts.urls')),
    path('schedule/', include('schedule.urls')),
    path('rounge/', include('rounge.urls')),
]
