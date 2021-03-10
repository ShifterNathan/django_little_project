from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name="Blog"),
    # path('categories/<category_id>/', views.categories, name="category") # To recognize it as a parameteer, it needs to be between "<>"

]