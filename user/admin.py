from django.contrib import admin
from user.models import Profile
from .models import SMSCode


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'age')
    fields = ('user', 'bio', 'avatar', 'age')



admin.site.register(SMSCode)