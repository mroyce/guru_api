from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from guru_api.core.auth.jwt import JWTLoginView, JWTSignUpView

from guru_api.core.views import UserProfileViewSet, InstructorProfileViewSet, CourseListingViewSet
from guru_api.apps.messaging.views import InboxViewSet, MessageViewSet


# Django REST framework API routing
router = DefaultRouter()

# Core
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'instructor-profiles', InstructorProfileViewSet)
router.register(r'course-listings', CourseListingViewSet)

# Messaging
router.register(r'inboxes', InboxViewSet)
router.register(r'messages', MessageViewSet)

# Payment


# Schedule


# Construct URLs
urlpatterns = [
	# API registration
	url(r'^api/', include(router.urls)),

	# Django admin views
    url(r'^api-admin/', include(admin.site.urls)),

    # API Authentication
    url(r'^api/auth/sign-up/', JWTSignUpView.as_view(), name='sign-up'),
    url(r'^api/auth/login/', JWTLoginView.as_view(), name='login'),
]

# DEBUG mode only URLs
if settings.DEBUG:
	urlpatterns += [
		# REST framework browsable API login/logout views
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

		# API documentation
		url(r'^api-docs/', include('rest_framework_swagger.urls')),
	]

	# Media files URL
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	# Static files URL
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
