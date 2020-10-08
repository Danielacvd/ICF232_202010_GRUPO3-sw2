from django.test import TestCase
from blogs import models

class ModelsTestCase(TestCase):
    blog = Blog.objects.create(title='Prueba')
    
