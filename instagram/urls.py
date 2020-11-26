from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home_view,name='homeView'),
    path('details/<int:pk>/',views.image_details,name='imageDetails'),
]