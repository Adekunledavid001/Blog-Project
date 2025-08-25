from django.shortcuts import render



# Create your views here.
from .models import BlogPost
def bloglist_page(request):

    all_blogs = BlogPost.objects.all().order_by("-Created_at") #Fetch all list from database

    context = {
        "blogs": all_blogs
    }

    return render(request,"blogs.html",context)

from django.template.defaultfilters import truncatewords


# def full_content_view(request):
#     all_blogs = BlogPost.objects.all() #Fetch all list from database

#     context = {
#         "blogs": all_blogs
#     }
#     # content = "This is a long piece of text that needs to be truncated to fit within a specific word limit for display purposes. It continues with more details that should only appear in the full view."
#     return render(request, 'full_content.html', context)




from .forms import BlogForm
from django.shortcuts import redirect
from django.contrib import messages
def createblog_page(request):

    if request.method == "POST":
        form = BlogForm(request.POST) #make request to post form
        if form.is_valid():
            form.save() #save form to database
            messages.success(request,"Your blog has been posted successfully!!")
            form = BlogForm() #reset
            return redirect("createblog")
    else:
        form = BlogForm()


    context ={
        "form": form
    }

    return render(request,"create.html",context)