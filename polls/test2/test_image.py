from django.test import TestCase

from polls.models import Product, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File


class SimpleTest(TestCase):
    def test_basic_addition(self):
        img = Image()

        img.name = "test3"

        img.pic = SimpleUploadedFile(name='test3', content=open("polls/test2/test3.png", 'rb').read(), content_type='image/png')
        #p = Image.objects.get(name='test2').pic.path
        #self.failUnless(open(p), 'file not found')

        #img.pic = File(open("polls/static/media/php.jpeg"))
        img.addImage()

        self.assertTrue(Image.objects.filter(name='test3').exists())

    def tearDown(self):
        Image.objects.get(name='test3').delete()


