from django.test import TestCase
from polls.models import Product, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import RequestFactory
from django.core.files import File
from polls.forms import UploadFileForm
import os


class SimpleTest2(TestCase):
    def setUp(self):
        self.img = Image()
        self.img.name = "test_image1"
        self.img.pic = SimpleUploadedFile(name=self.img.name, content=open("polls/test2/test_image.png", 'rb').read(), content_type='image/png')
        self.img2 = Image()
        self.img2.name = "test_image222"
        self.img2.pic = SimpleUploadedFile(name=self.img2.name, content=open("polls/test2/test_image.png", 'rb').read(), content_type='image/png')
        self.product_info1 = {'name': "Intro to algorithm", "pic":  "polls/test2/test_image.png"}
        self.img2.addImage()
        self.factory = RequestFactory()

    def test_addImage(self):
        self.img = Image()
        self.img.name = "test_image333"
        self.img.addImage()
        self.assertTrue(Image.objects.filter(name='test_image333').exists())

    def test_addImage2(self):
        img = Image()
        img.name = "test_image444"
        img.addImage()
        self.assertTrue(Image.objects.filter(name='test_image444').exists())

    def test_getUrl(self):
        self.assertEqual("/media/test_image222", self.img2.getUrl())

    def tearDown(self):
        Image.objects.get(name='test_image222').delete()
        #Image.objects.get(name='test_image1').delete()
        #os.remove("polls/static/media/test_image1")
        os.remove("polls/static/media/test_image222")
        #os.remove("polls/static/media/test_image1")
        


