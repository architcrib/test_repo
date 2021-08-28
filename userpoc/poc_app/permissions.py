
from rest_framework.permissions import BasePermission


class IsOperator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_operator: # and request.user.groups.filter(name='customers'):
            return True
        return False


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_tenant: # and request.user.groups.filter(name='staff'):
            return True
        return False