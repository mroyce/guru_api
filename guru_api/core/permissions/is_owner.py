from django.conf import settings

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Only the owner can edit and view this object
    """
    def has_object_permission(self, request, view, obj):
        """
        This permission checks that the current user is owner of the object
        or if the current user is the compared object.
        """
        # Check if this object belongs to either the user or organization
        account = request.user
        check_user = (getattr(obj, 'user', obj) == getattr(account, 'user', account))
        check_organization = (getattr(obj, 'organization', obj) == getattr(account, 'organization', account))

        return check_user or check_organization
