from rest_framework.permissions import BasePermission,SAFE_METHODS,IsAdminUser




class IsOwnerPermissionOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.author==request.user


