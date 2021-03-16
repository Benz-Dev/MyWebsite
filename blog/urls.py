from django.urls import path
from .views import *

urlpatterns = [
     path('', Articles, name="blog"),
     path('<slug>', Post, name="article"),
     path('categoria/<category>', search_category, name="categorys")
]