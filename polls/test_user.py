#tests.py
#import models
from django.test import TestCase, TransactionTestCase, Client
from django.contrib.auth.models import User

class test_log_in(TestCase):
    def setUp(self):
        User.objects.create_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        
    def test_log_in(self):
     
        login = self.client.login(username='temporary@gmail.com', password='temporary')
        self.assertTrue(login) 

        #self.assertEqual(response.context['E'], 'temporary@gmail.com')


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.sample_user = RegistrationProfile.objects.create_inactive_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.expired_user = RegistrationProfile.objects.create_inactive_user('temporary@gmail.com', 'temporary@gmail.com', 'temporary')
        self.expired_user.date_joined -= datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS + 1)
        self.expired_user.save()


