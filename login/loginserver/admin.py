from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from loginserver.models import average_user
# Register your models here.

class average_userInline(admin.TabularInline):#两张表连在一起
    model = average_user
    can_delete = False
    verbose_name_plural = 'average_user'

class UserAdmin(BaseUserAdmin):
    inlines = (average_userInline,)

admin.site.unregister(User) #取消之前的注册
admin.site.register(User,UserAdmin) #重新注册