from django.urls import path
from . import views

urlpatterns = [
    path('addlaptop/',views.addlaptopmodel,name='add_laptop'),
    path('showlaptop/',views.showlaptop,name='show_laptop'),
    path('delete/<int:i>/',views.deletelaptop,name='delete_laptop'),
    path('update/<int:i>/',views.updatelaptop,name='update_laptop'),
]