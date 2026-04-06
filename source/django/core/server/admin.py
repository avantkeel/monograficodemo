from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Determines which columns appear
    list_display = ('id', 'username', 'email', 'firstname', 'lastname', 'passwordhash')
    
    ordering = ('id',)
    search_fields = ('username', 'email')
    
    list_filter = ('id',)
