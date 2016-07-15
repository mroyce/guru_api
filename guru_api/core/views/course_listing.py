from rest_framework import viewsets

from guru_api.core.models import CourseListing
from guru_api.core.serializers import CourseListingSerializer


class CourseListingViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `CourseListing` Model
    """
    queryset = CourseListing.objects.all()
    serializer_class = CourseListingSerializer
    filter_fields = ()
