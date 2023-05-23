from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name",'who_i','price')


# admin.site.register(Profile , ProfileAdmin)