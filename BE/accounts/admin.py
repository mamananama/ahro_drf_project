from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'email',
    )

    list_display_links = (
        'username',
        'email',
    )
