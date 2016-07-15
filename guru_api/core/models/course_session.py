from django.db import models

from guru_api.core.base.model import BaseGuruModel


class CourseSession(BaseGuruModel):
    """
    CourseSession Model
    """
    course_listing = models.ForeignKey('core.CourseListing', related_name='course_sessions')
    user = models.ForeignKey('core.User', related_name='course_sesions')

    date = models.DateTimeField()
    paid = models.BooleanField(blank=True, default=False)
