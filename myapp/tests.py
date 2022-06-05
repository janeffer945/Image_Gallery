
  
from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class GalleryTest(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='food')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'kenya')
        self.new_location.save_location()
        self.new_image = Image(id=1,img_name='apples', img_decription='this is an apple',img_path='media/pictures/apples-1776744_1920.jpg',img_category=self.new_category,img_location=self.new_location)

