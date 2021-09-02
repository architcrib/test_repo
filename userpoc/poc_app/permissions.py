
from rest_framework.permissions import BasePermission


class IsOperator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_operator


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_tenant


class IsSpecialOperator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_operator and request.user.groups.filter(name='SpecialOperators')


class IsLegit(BasePermission):
    def has_permission(self, request, view):
        op = Operator.objects.get(user= user)
        if op.roles != 'warden':
            raise PermissionError
