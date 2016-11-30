from django.test import TestCase

from polls.models import Product, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

class SimpleTest(TestCase):
    def test_basic_addition(self):
        img = Image()

        img.name = "test1"

        img.pic = SimpleUploadedFile(name='test1', content=open("polls/static/media/php.jpeg", 'rb').read(), content_type='image/jpeg')


        #img.pic = File(open("polls/static/media/php.jpeg"))
        img.addImage()

        
        
        #self.assertEqual(Image.objects.count(), 1)
        p = Image.objects.get(name='test1').pic.path
        print(p)
        #self.assertEqual(Image.objects.get(name='test1').pic.path, "polls/static/media/php.jpeg")
        
        self.failUnless(open(p), 'file not found')
        self.assertTrue(Image.objects.get(name='test1').pic.path)

