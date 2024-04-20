from rest_framework import permissions
from rest_framework.views import View
from rest_framework.request import Request

from users.models import User


class AdminPermission(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, user: User
    ) -> bool:  # noqa
        if request.user.is_superuser or request.user.id == user.id:
            return True
