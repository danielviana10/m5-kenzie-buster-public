from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import View


class EmployeePermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_employee
