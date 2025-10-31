from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # admin allowed to do anything
        if request.user.is_staff or getattr(request.user, 'is_admin', False):
            return True
        # allow only blog owner to edit/delete
        return obj.author == request.user