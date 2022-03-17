from django.contrib import admin

# Register your models here.
from .models import Users
# admin.site.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Users,UserAdmin)

