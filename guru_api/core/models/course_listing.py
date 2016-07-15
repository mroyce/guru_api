from django.db import models

from guru_api.core.base.model import BaseGuruModel


class CourseListing(BaseGuruModel):
    """
    CourseListing Model
    """
    instructor_profile = models.ForeignKey('core.InstructorProfile', related_name='course_listings')

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    cancellation_fee = models.DecimalField(decimal_places=2, max_digits=9, blank=True, default=0)
