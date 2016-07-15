from django.conf import settings

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Only the owner can edit the object
    """
    def has_object_permission(self, request, view, obj):
        """
        This permission checks that the current user is owner of the object
        or if the current user is the compared object.
        Allows any user to view this object.
        """
        # If the request method is 'GET', 'OPTIONS', or 'HEAD', allow access to this endpoint
        if request.method in SAFE_METHODS:
            return True

        # Check if this object belongs to either the user or organization
        account = request.user
        check_user = (getattr(obj, 'user', obj) == getattr(account, 'user', account))
        check_organization = (getattr(obj, 'organization', obj) == getattr(account, 'organization', account))

        return check_user or check_organization
