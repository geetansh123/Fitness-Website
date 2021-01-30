from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput,Textarea

# Register your models here.
from .models import NewUser

class UserAdminConfig(UserAdmin):

    model=NewUser

    search_fields = ('email', 'user_name', 'first_name',)
    list_filter=('email','user_name','first_name','is_active','is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal',{'fields':('about','age','gender','blood_group','height','weight','goal')}),
    )
    formfields_overrides = {
        NewUser.about:{'widget':Textarea(attrs={'rows':10,'cols':40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('email','user_name','first_name','age','gender','blood_group','height','weight','goal','password1','password2','is_active','is_staff')
        }),
    )

admin.site.register(NewUser,UserAdminConfig)