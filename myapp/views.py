from django.shortcuts import render
from .models import Image,Category,Location
# pagination
from django.core.paginator import Paginator
# Create your views here.
def display(requests):
    all_images= Image.objects.all()
    locations=Location.objects.all()
    categories=Category.objects.all()
    # Set up Pagination
    p = Paginator(Image.objects.all(), 12)
    page = requests.GET.get('page')
    images_all = p.get_page(page)
    nums = "a" * images_all.paginator.num_pages
