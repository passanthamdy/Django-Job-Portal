from django.contrib import admin
from .models import Job
# Register your models here.
# admin.site.register(Job)
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    
    list_display=['id','name','job_owner','description','creation_time','modification_time','get_tags','get_developers']
    fieldsets=(
        ('Job Info',{'fields':['name','job_owner','developer','status']}),
        ('Extra Info',{'fields':['description','Tags','applied_developers']}),
    )
    
    
    def get_tags(self, obj):
        if obj.Tags.all():
            return list(obj.Tags.all().values_list('name', flat=True))
        else:
            return 'No Tags Yet...'
    def get_developers(self, obj):
        if obj.applied_developers.all():
            return list(obj.applied_developers.all().values_list('username', flat=True))
        else:
            return 'No Developers Yet...'
        
    get_tags.short_description='tags names'
    get_developers.short_description='developers names'


    # def has_delete_permission(self,request,obj=None):
    #     if request.user.is_superuser:
    #         return False
    #     return True
        
    # def has_change_permission(self,request,obj=None):
    #     if request.user.is_superuser:
    #         return False
    #     return True
    
   
        
    # filter_horizontal=['tags']           


