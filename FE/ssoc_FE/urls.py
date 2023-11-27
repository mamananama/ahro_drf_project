from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('accounts.urls')),
    path('schedule/', include('schedule.urls')),
    path('rounge/', include('rounge.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += re_path(r'^media/(?P<path>.*)$', serve,
                       {'document_root': settings.MEDIA_ROOT}),
urlpatterns += re_path(r'^static/(?P<path>.*)$', serve,
                       {'document_root': settings.STATICFILES_DIRS[0]}),
