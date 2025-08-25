from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["Blog_Title","Content","Blog_Category","Author","Email_Address"]
        widgets = {
            "Blog_Title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter blog title",
                "required": True,
            }),
            "Content": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write your blog content here...",
                "rows": 5,
                "required": True,
            }),
            "Blog_Category": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter blog Category",
                "required": True
            }),
            "Author": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Author's name",
                "required": True
            }),
            "Email_Address": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": 'your@email.com',
                "required": True
            })
        }