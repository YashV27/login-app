from django.contrib import admin

from .models import User,UserInfo,UserImages

class Info(admin.StackedInline):
    model = UserInfo
    extra = 1

class Images(admin.StackedInline):
    model = UserImages
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines=[Info,Images]

admin.site.register(User,UserAdmin)

search_fields = ['Username','Firstname','Lastname','Enroll','email']
