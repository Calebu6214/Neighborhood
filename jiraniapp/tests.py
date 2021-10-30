from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

import datetime as dt
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.kibra = neighbourhood(neighbourhood='kibra')

    def test_instance(self):
        self.assertTrue(isinstance(self.kibra,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.kibra.save_neighbourhood()
        jirani = neighbourhood.objects.all()
        self.assertTrue(len(jirani)>0)
