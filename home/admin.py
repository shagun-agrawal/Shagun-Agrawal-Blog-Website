from django.contrib import admin
from .models import User,Data
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','email','username','password','confirm_password','birthdate')
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display=('id','title_name','title','photo')

