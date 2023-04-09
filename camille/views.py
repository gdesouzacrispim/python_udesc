from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    p = Post.objects.all()
    return render(request, 'camille/post_list.html', {'posts':p})
