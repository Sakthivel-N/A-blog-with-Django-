from django.shortcuts import render
from .models import Post

def index(request):
    posts=Post.objects.all()
    return render (request,'index.html',{'posts':posts})

def post_details(request,idval):
    posts=Post.objects.get(id=idval)
    return render(request,'posts.html',{'posts':posts})
