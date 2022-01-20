from django.shortcuts import render
from gallery.models import *

# Create your views here.
def author(request):
    posts = Blog.objects.all()
    return render(request, 'user/author.html', {'posts':posts})