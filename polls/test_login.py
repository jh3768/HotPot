#tests.py
#import models
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestUser(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username = 'temporary@gmail.com', email = 'temporary@gmail.com', last_name = 't', first_name = 'm', password = 'temporary')
        self.user2 = User.objects.create_user(username = 'invalid_email_address', email='invalid_email_address', password = 'temporary', last_name = 't', first_name = 'm')
        self.user3 = User.objects.create_user(username = 'user3', email='', password = 'temporary', last_name = 't', first_name = 'm')
        self.user4 = User.objects.create_user(username = '', email='user4@columbia.edu', password = 'temporary', last_name = 't', first_name = 'm')
        self.user5 = User.objects.create_user(username = 'user5', email='user5@gmail.com', password = '', last_name = 't', first_name = 'm')
        #self.user6 = User.objects.create_user(username = 'user6', email='user6@gmail.com', password = 'temporary', last_name = '', first_name = 'm')
        #self.user7 = User.objects.create_user(username = 'user7', email='user7@gmail.com', password = 'temporary', last_name = 'user', first_name = '')
        self.user8 = User.objects.create_user(username = 'user8', email = 'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww@wwwwwwwwwwwwwwwwwwwwwwwwwwww.com',  password = 'temporary', last_name = 't', first_name = 'm')
        #self.user9 =  User.objects.create_user(username ='', email = '', password = '', first_name = '', last_name = '')
        #self.user10 =  User.objects.create_user(username ='I do not have last name', email = 'user10@gmail.com', password = 'temporary', first_name = 'ff')
        #self.user11 = User.objects.create_user(username ='I do not have first name', email = 'user11@gmail.com', password = 'temporary', last_name = 'll')
        
        self.user12 = User.objects.create_user(username = 'temporary2@columbia.com', email = 'temporary2@columbia.com', last_name = 'temp', first_name = 'orary', password = 'temporary')
        self.user13 = User.objects.create_user(username = 'invalid_email_address2', email='no at', password = 'temporary', last_name = 't', first_name = 'm')
        self.user14 = User.objects.create_user(username = 'user14', email=' ', password = 'temporary', last_name = 't', first_name = 'm')
        self.user15 = User.objects.create_user(username = ' ', email='user15@columbia.edu', password = 'temporary', last_name = 't', first_name = 'm')
        self.user16 = User.objects.create_user(username = 'user16', email='user5@gmail.com', password = '', last_name = 't', first_name = 'm')
        self.user17 = User.objects.create_user(username = 'user17', email='user6@gmail.com', password = 'temporary', last_name = '', first_name = 'm')
        #self.user18 = User.objects.create_user(username = 'user18', email='user18@gmail.com', password = 'temporary', last_name = ' ', first_name = '')
        self.user19 = User.objects.create_user(username = 'user19', email ='wfjwgh3409t3ggh4ohj4h045h04uh945hi4509hu409hu490hu490hu049h90j2oije2hr293 hrh23hr9023ur0923ur230hr2h092r023ur23rh23rh239hr2rh289h289rh2389h2389rh2rj2rh9wefwo32@gmail.com', password = 'temporary', last_name = 't', first_name = 'm')
        #self.user20 =  User.objects.create_user(username ='no last name', email = 'user20@gmail.com', password = 'temporary', first_name = 'gwge')
        #self.user21 = User.objects.create_user(username ='no first name', email = 'user21@gmail.com', password = 'temporary', last_name = 'egerge')
        #self.user22 = User.objects.create_user(username = 'user22', email='user22@gmail.com', password = 'temporary', last_name = 'user', first_name = ' ')

        self.c = Client()

    def test_login_user1(self):
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        self.user1 = User.objects.get(username='temporary@gmail.com')
        "test if a user is able to log in"
        self.assertTrue(self.login)
        "test if a user is authenticated"
        self.assertIn('_auth_user_id', self.c.session)
        "test if the user has the same passowrd and username from initialization"
        self.assertEqual(self.user1.username, 'temporary@gmail.com')
        self.assertEqual(self.user1.email, 'temporary@gmail.com')
        
    def test_login_user2(self):
        self.login = self.c.login(username='temporary2@gmail.com', password='temporary')
        self.user1 = User.objects.get(username='temporary2@gmail.com')
        self.assertTrue(self.login)
        self.assertIn('_auth_user_id', self.c.session)
        self.assertEqual(self.user2.username, 'temporary2@gmail.com')
        self.assertEqual(self.user2.email, 'temporary2@gmail.com')
        
    def test_login_status1(self):
        "test if the above user is logged in"
        self.login = self.c.login(username='temporary@gmail.com', password='temporary')
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)
        
    def test_login_status2(self):
        "test if the above user is logged in"
        self.login = self.c.login(username='temporary2@gmail.com', password='temporary')
        response = self.c.get('/polls/profile/', follow=True)
        self.assertEqual(response.status_code, 200)    
        
    def test_user_invalid_email_address1(self):
        self.login = self.c.login(username='invalid_email_address', password='temporary')
        self.assertFalse(self.login)
    
    def test_user_invalid_email_address2(self):
        self.login = self.c.login(username='invalid_email_address2', password='temporary')
        self.assertFalse(self.login) 
        
    def test_user_invalid_long_email1(self):
        self.login = self.c.login(username='user8', password='temporary')
        self.assertFalse(self.login)
        
    def test_user_invalid_long_email2(self):
        self.login = self.c.login(username='user19', password='temporary')
        self.assertFalse(self.login)    
                      
#     def test_user_no_last_name1(self):
#         self.login = self.c.login(username='I do not have last name', password='temporary')
#         self.assertFalse(self.login)
#         
#     def test_user_no_last_name2(self):
#         self.login = self.c.login(username='I do not have last name', password='temporary')
#         self.assertFalse(self.login)    
#         
#     def test_user_no_first_name(self):
#         self.login = self.c.login(username='I do not have first name', password='temporary')
#         self.assertFalse(self.login)
        
    
                   
