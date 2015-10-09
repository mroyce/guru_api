from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from django_rest_skeleton.core.views import UserViewSet


# Django REST framework API routing
router = DefaultRouter()

# API endpoints
router.register(r'users', UserViewSet)

# Construct URLs
urlpatterns = patterns(
	'',

	# API registration
	url(r'^api/', include(router.urls)),

	# Django admin views
    url(r'^api-admin/', include(admin.site.urls)),
)

# DEBUG mode only URLs
if settings.DEBUG:
	urlpatterns += patterns (
		'',

		# REST framework browsable API login/logout views
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

		# API documentation
		url(r'^api-docs/', include('rest_framework_swagger.urls')),
	)

	# Media files URL
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	# Static files URL
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
