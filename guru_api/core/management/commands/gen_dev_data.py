import os
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings

from guru_api.core.models import User, InstructorProfile, CourseListing
from guru_api.apps.messaging.models import Inbox, Message

from guru_api.core.tests.helpers import (create_test_user, create_test_instructor_profile, create_test_education,
                                         create_test_experience, create_test_credential, create_test_course_listing)
from guru_api.apps.messaging.tests.helpers import create_test_inbox, create_test_message


class Command(BaseCommand):
    """
    gen_dev_data command
    Generate data for our local development environments.
    """
    def handle(self, *args, **kwargs):
        """
        Run gen_dev_data command
        """
        # Only run this command in development environment
        if not settings.DEBUG:
            print 'Only run this in development environment!'
            return

        # Delete previous files in `/media/`
        print 'Deleting existing media files'
        folder = settings.MEDIA_ROOT
        if os.path.isdir(folder):
            shutil.rmtree(folder)

        #################### 1. USERS ####################
        print 'Creating Users',

        user_maurice = create_test_user(
            email='maurice@dickinson.edu',
            password='test',
            first_name='Maurice',
            last_name='Royce',
            gender='M',
        )
        print '.',

        user_tim = create_test_user(
            email='tim@dickinson.edu',
            password='test',
            first_name='Tim',
            last_name='Kang',
            gender='M',
        )
        print '.',

        user_john = create_test_user(
            email='johng307@gmail.com',
            password='test',
            first_name='John',
            last_name='G',
            gender='M',
        )
        print '.',

        user_alpha = create_test_user(
            email='alpha@example.com',
            password='test',
            first_name='Alpha',
            last_name='Smith',
        )
        print '.',

        user_bravo = create_test_user(
            email='bravo@example.com',
            password='test',
            first_name='Bravo',
            last_name='Smith',
        )
        print '.'

        #################### 2. INSTRUCTORS ####################
        print 'Creating Instructors',

        instructor_profile_alpha = create_test_instructor_profile(
            user=user_alpha,
            biography=("I grew up in Honolulu, Hawaii and began piano lessons at the age of 6.  I performed in countless studio recitals, christmas concerts, mall performances, evaluations, and competitions (where I won second place in the Hawaii Music Teachers Association State Competition).  I also played the tenor saxophone in middle and high school, performing in the Wind Ensemble, Marching Band (performed at the Holiday Bowl), Jazz Band, Solo & Ensemble Festival, and the All-State Marching Band, which performed in the Macy's Day Parade.  Through high school, I thoroughly enjoyed making music at every opportunity possible.\n"
                       "However, I thought that music was just a hobby of mine.  I attended UCLA and graduated with honors, but with a Bachelor of Science degree in Psychobiology.  I thought I was going to be a pharmacist.  Yet, I kept finding myself in new musical endeavors -- nothing could tear me away from the music.\n"
                       "I spent the next three years on the Japan Exchange and Teaching (JET) Program in Nara, Japan.  My musical experiences expanded even more as I helped my school's concert band in competitions and also helped organize a performance in the annual JETNet International Arts Festival, which highlighted international exchange between the Japanese people and foreigners.\n"
                       "I am currently a member of the California Association of Professional Music Teachers (CAPMT), Music Teachers National Association (MTNA), and Music Teachers Association of California (MTAC).  I currently teach over 50 students (including appoximately 15 adult students!).\n"
                       "It is this passion for music that led me into it full time.  Why not make something you already willingly do so much into a career?  And so here I am."),
            website='http://www.gkpiano.com/',
            trial_lesson=True,
        )
        print '.',

        instructor_profile_bravo = create_test_instructor_profile(
            user=user_bravo,
            biography=("I like to teach stuff."),
            website='http://www.google.com',
            will_travel=True,
        )
        print '.'

        ################## 3. COURSE LISTINGS ##################
        print 'Creating Course Listings',

        alpha_course_listing_1 = create_test_course_listing(
            instructor_profile=instructor_profile_alpha,
            title='Piano Lessons for All Ages',
            description=("My background is primarily classical, but I include other styles of music in my performance and teaching repertoire, including blues, popular, Broadway, and more. My teaching is based in the classical piano method, which includes keyboard technique, varied repertoire, theory and music reading. Various styles of music can be included for those who want to branch out beyond the classical genre.\n"
                         "Music is an avenue of expression, a satisfying emotional outlet, a source of spiritual support, fun, and more. Students work at lessons, but lessons should also be fun. I believe in providing patience and support. I find it satisfying to work with students of any age, and I especially enjoy children. Through music study we learn to play an instrument, and we also learn to enjoy music throughout our lives.\n"
                         "I studied in Los Angeles and later in Boston at the New England Conservatory of Music. I have worked as an accompanist; conductor for several Bay Area organizations; as a teacher in music/rhythm classes for young children; and as a vocal soloist with various organizations in the Bay Area and Boston. References and resume are available."),
            cancellation_fee=5,
        )
        print '.',

        alpha_course_listing_2 = create_test_course_listing(
            instructor_profile=instructor_profile_alpha,
            title='Group Piano Lessons for All Ages',
            description='Group piano lessons cost less money but are less personalized.',
            cancellation_fee=5,
        )
        print '.'

        #################### 4. MESSAGING ####################
        print 'Creating Messages',


        print '.'

        #################### FINAL OUTPUT ####################
        print '-------------------- Users --------------------'
        print 'There are {} test users:'.format(User.objects.count())
        for user in User.objects.all():
            print ' * User {}:'.format(user.id)
            print '     - email: {}'.format(user.email)
            print '     - name: {}'.format(user.first_name)

        print '----------------- Instructors -----------------'
        print 'There are {} test instructor profiles:'.format(InstructorProfile.objects.count())
        for instructor_profile in InstructorProfile.objects.all():
            print ' * Instructor Profile {}:'.format(instructor_profile.id)
            print '     - user: {}'.format(instructor_profile.user.first_name)

        print '--------------- Course Listings ---------------'
        print 'There are {} test class listings:'.format(CourseListing.objects.count())
        for course_listing in CourseListing.objects.all():
            print ' * Class Listing {}:'.format(course_listing.id)
            print '     - title: {}'.format(course_listing.title)

        print '------------------ Messaging ------------------'
        print 'There are {} test inboxes'.format(Inbox.objects.count())
        print '      and {} test messages:'.format(Message.objects.count())
        for inbox in Inbox.objects.all():
            print ' * Inbox {}'.format(inbox.id)
            print '     - users:'
            for account in inbox.accounts.all():
                print '     -email: {}'.format(account.email)
