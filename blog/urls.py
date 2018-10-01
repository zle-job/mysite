from django.urls import path

from .views import *

urlpatterns = [
    # http://ip:port/blog/
    path('', blog_list, name='blog_list'),
    # http://ip:port/blog/blog_pk
    path('<int:blog_pk>', blog_detail, name='blog_detail'),
    path('category/<int:blogs_category>', blogs_with_category, name='blogs_with_category'),

]
