from django.contrib import admin
from authentification.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(User, UserAdmin)