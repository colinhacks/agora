from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cityapp.models import City

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	hometown = models.ForeignKey('cityapp.City',related_name='residents',default=None,null=False,blank=False)

"""class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
"""
admin.site.register(UserProfile)
