from django.conf import settings

from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowSafeMethods(BasePermission):
	"""
	Only allow unauthenticated requests from the permissions.SAFE_METHODS list
	'GET', 'OPTIONS', 'HEAD'
	"""
	def has_permission(self, request, view):
		# If the request method is 'GET', 'OPTIONS', or 'HEAD', allow access to this endpoint
		if request.method in SAFE_METHODS:
			return True

		# If Django is in DEBUG mode, allow access to this endpoint
		if settings.DEBUG:
			return True

		return False
