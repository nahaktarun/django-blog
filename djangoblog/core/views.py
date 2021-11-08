from django.shortcuts import render

# Create your views here.
from blog.models import Post

def frontpage(request):
    posts = Post.objects.filter(status = Post.ACTIVE)
    return render(request, 'core/frontpage.html', {"posts": posts})


def aboutpage(request):
    return render(request, 'core/about.html') 

