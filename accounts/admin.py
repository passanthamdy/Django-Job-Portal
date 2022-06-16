from django.contrib import admin
from .models import User


# Register your models here.

@admin.register(User)
<<<<<<< HEAD
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','user_type', 'gender', 'dob', 'company_name', 'cv', 'address', 'get_tags', 'get_history',
                    'is_active']

    search_fields = ( 'username','user_type', 'gender',)
    fieldsets = (
        ('Personal Info', {
            'fields': ['username', 'first_name', 'last_name', 'password', 'user_type', 'gender', 'address', 'dob',
                       'company_name', 'is_active']}),
        ('Upload Section', {'fields': ['cv']}),
        ('Extra Info', {'fields': ['tags', 'history', ]}),
=======

class UserAdmin(admin.ModelAdmin):
   
    
    list_display = ['id','username','email','user_type','gender','dob','company_name','cv','address','get_tags','get_history','is_active']

    search_fields = ('user_type','gender',)
    fieldsets=(
        ('Personal Info',{'fields':['username','email','first_name','last_name','password','user_type','gender','address','dob','company_name','is_active']}),
        ('Upload Section',{'fields':['cv']}),
        ('Extra Info',{'fields':['tags','history',]}),
>>>>>>> 39d48cef46770203003645ed653cabc55341ed14
    )

    def get_tags(self, obj):
        if obj.tags.all():
            return list(obj.tags.all().values_list('name', flat=True))
        else:
            return 'No Tags Yet...'
<<<<<<< HEAD

    get_tags.short_description = 'tags names'

=======
    get_tags.short_description='tags names'
    
>>>>>>> 39d48cef46770203003645ed653cabc55341ed14
    def get_history(self, obj):
        if obj.history.all():
            return list(obj.history.all().values_list('name', flat=True))
        else:
            return 'No History Yet...'
<<<<<<< HEAD

    get_history.short_description = 'History'

    class Meta:
        model = User
=======
    get_history.short_description='History'
     
    
        

    class Meta:
        model = User






>>>>>>> 39d48cef46770203003645ed653cabc55341ed14
