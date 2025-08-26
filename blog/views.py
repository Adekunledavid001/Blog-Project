from django.shortcuts import render
from .models import BlogPost
from .forms import BlogForm
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404




# Create your views here.

def home_page(request):
    posts = BlogPost.objects.all().order_by("-Created_at")[:3] # latest first
    
    context = {
        "posts": posts
    }
    return render(request,"index.html",context)




def bloglist_page(request):
    all_blogs = BlogPost.objects.all().order_by("-Created_at") #Fetch all list from database

    context = {
        "blogs": all_blogs
    }
    return render(request,"blogs.html", context)
# From the html through the link's herf a request and pk is passed into the viewpage and url

# to create full content or read more
def full_content_page(request, pk):
    # Through the primary key or id, the exact row is located and accessed by get_object_or_404 from the database 
    posts = get_object_or_404(BlogPost, id= pk)  

    context = {
        "posts": posts
    }
    return render(request,"full_content.html",context)




def createblog_page(request):
    if request.method == "POST":
        form = BlogForm(request.POST) #make request to post form
        if form.is_valid():
            form.save() #save form to database
            messages.success(request,"Your blog has been posted successfully!!") #send message
            form = BlogForm() #reset
            return redirect("createblog")
    else:
        form = BlogForm()

    context ={
        "form": form
    }
    return render(request,"create.html",context)



# UPDATE
# id, pk are primary key. unique identifier
def blog_update_page(request,pk):
    blog = get_object_or_404(BlogPost, id=pk)
    if request.method == "POST":    
        form = BlogForm(request.POST, instance=blog) #make request to post form
        if form.is_valid():
            form.save() #save form to database
            messages.success(request,"update successful!!")
            form = BlogForm() #reset
            return redirect("blogs")
    else:
        form = BlogForm(instance=blog)

    return render(request,"blog_update.html",{"form":form})



# DELETE
def blog_delete_page(request,pk):
    blog = get_object_or_404(BlogPost,id=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request,"Delete successful!!")
        return redirect("blogs")

    return render(request,'full_content.html',{"blog":blog})


