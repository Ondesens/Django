from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import BlogPost, Comment,  ContactMessage

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Permission)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "message")