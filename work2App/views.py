from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from blog.models import BlogPost

def home_page(request):
    
    posts = BlogPost.objects.all().order_by("-Created_at")[:3] # latest first
    
    context = {
        "posts": posts
    }
    return render(request,"index.html",context)

