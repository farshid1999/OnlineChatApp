from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ChatGroup)
class AdminChatGroup(admin.ModelAdmin):
    pass

@admin.register(GroupMessage)
class AdminChatGroup(admin.ModelAdmin):
    pass



