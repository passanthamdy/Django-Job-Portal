from django.contrib import admin
from .models import User
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'id']
#     class Meta:
#         model = User

# admin.site.register(User, UserAdmin)

admin.site.register(User)
