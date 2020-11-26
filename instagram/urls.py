from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='homeView'),
    path('details',views.image_details,name='imageDetails'),
]