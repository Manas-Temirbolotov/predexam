from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSenderPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and request.user.profile.is_sender)
                    )


class IsBuyerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    (request.user and request.user.is_authenticated and not request.user.profile.is_sender)
                    )


class IsOwnerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_authenticated and
             request.user.profile == obj.profile)
        )