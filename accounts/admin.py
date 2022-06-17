from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'user_type', 'gender', 'dob', 'company_name', 'cv', 'address', 'get_tags',
                    'is_active', 'allow_notification']

    search_fields = ('username', 'user_type', 'gender',)
    fieldsets = (
        ('Personal Info', {
            'fields': ['username', 'email', 'first_name', 'last_name', 'password', 'user_type', 'gender', 'address',
                       'dob',
                       'company_name', 'is_active']}),
        ('Upload Section', {'fields': ['cv']}),
        ('Extra Info', {'fields': ['tags', 'allow_notification', 'history','in_job']}),)

    def get_tags(self, obj):
        if obj.tags.all():
            return list(obj.tags.all().values_list('name', flat=True))
        else:
            return 'No Tags Yet...'

    get_tags.short_description = 'tags names'

    def get_history(self, obj):
        if obj.history.all():
            return list(obj.history.all().values_list('name', flat=True))
        else:
            return 'No History Yet...'

    get_history.short_description = 'History'

    class Meta:
        model = User
