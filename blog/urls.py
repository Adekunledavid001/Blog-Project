from django.urls import path
from . import views

urlpatterns = [
    path("blogs/",views.bloglist_page,name='blogs'),
    path("createblog/",views.createblog_page,name="createblog"),
]