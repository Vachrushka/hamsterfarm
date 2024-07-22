from django.contrib import admin
from .models import *


@admin.register(Access)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'token')
    readonly_fields = ('token', 'created_at')
    fields = ('access', 'created_at', 'token')
    list_filter = ('access',)
    search_fields = ('token',)
    filter_horizontal = ('access',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.save()
        super().save_model(request, obj, form, change)

admin.site.register(Token, TokenAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('tokens',)
