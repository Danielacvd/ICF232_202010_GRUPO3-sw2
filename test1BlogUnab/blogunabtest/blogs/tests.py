from django.test import TestCase
from models import Blog

# Create your tests here.
class ModelsTestCase(TestCase):
    blog = Blog.objects.create(title='Prueba')
    
