from django.db import models

# Create your models here.

class BlogPost(models.Model):
    Blog_Title = models.CharField(max_length=200)
    Content = models.TextField()
    Blog_Category = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Email_Address = models.EmailField(default="your@email.com")
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Blog_Title} written by {self.Author}"
    