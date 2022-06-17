from rest_framework import permissions

class JobOwnerPermission(permissions.BasePermission):
    message = 'Editing or updating is restricted to the current user only.'
    print('entered permission')
    def has_permission(self, request, view):
        print('ooo')
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        print(obj.job_owner)
        return obj.job_owner == request.user
        

        #return obj.job_owner == request.user


class IsEditor(permissions.BasePermission):
   def has_permission(self, request, view):
      return request.user.is_editor