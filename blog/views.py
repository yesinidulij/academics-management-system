from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts=[
    {
        'author':'kefiyalew',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 27, 2018'
    },
      {
        'author':'Netsanet',
        'title':'Blog Post 1',
        'content':'second post content',
        'date_posted':'August 28, 2018'
    }
]

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html','titlle')