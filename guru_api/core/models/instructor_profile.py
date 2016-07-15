from django.db import models

from guru_api.core.base.model import BaseGuruModel


class InstructorProfile(BaseGuruModel):
    """
    Instructor Model
    """
    user = models.OneToOneField('core.User', related_name='instructor_profile')

    biography = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    # (list)(???) fields of teaching
        # (music)(languages)(tutoring)(sports)
    # (schedule model) schedule/availability
    is_active = models.BooleanField(default=True)
    will_travel = models.BooleanField(default=False)
    trial_lesson = models.BooleanField(default=False)

    def delete(self):
        """
        Don't delete the InstructorProfile
        Instead just set `is_active` to False
        """
        self.is_active = False
        self.save()
        return self


class Education(models.Model):
    """
    Education Model
    """
    HIGH_SCHOOL = 1
    ASSOCIATES = 2
    BACHELORS = 3
    MASTERS = 4
    PHD = 5
    MBA = 6
    JD = 7
    MD = 8
    OTHER = 9

    DEGREE_CHOICES = (
        (HIGH_SCHOOL, 'High School'),
        (ASSOCIATES, 'Associate\'s Degree'),
        (BACHELORS, 'Bachelor\'s Degree'),
        (MASTERS, 'Master\'s Degree'),
        (PHD, 'Doctor of Philosophy (Ph. D.)'),
        (MBA, 'Master of Business Administration (M.B.A.)'),
        (JD, 'Juris Doctor (J.D.)'),
        (MD, 'Doctor of Medicine (M.D.)'),
        (OTHER, 'Other'),
    )

    instructor_profile = models.ForeignKey('core.InstructorProfile', related_name='education')

    school = models.CharField(max_length=255)
    year_started = models.IntegerField(blank=True, null=True)
    year_ended = models.IntegerField(blank=True, null=True)
    degree_type = models.PositiveSmallIntegerField(choices=DEGREE_CHOICES, blank=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Experience(models.Model):
    """
    Experience Model
    """
    instructor_profile = models.ForeignKey('core.InstructorProfile', related_name='experience')

    role = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    year_started = models.IntegerField(blank=True, null=True)
    year_ended = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Credential(models.Model):
    """
    Credentials Model
    """
    instructor_profile = models.ForeignKey('core.InstructorProfile', related_name='credentials')

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)