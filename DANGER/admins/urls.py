from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    
    path('list_admin/', views.list_Admin, name="list_admin"),
    path('update_admin/<admin_id>/', views.update_admin, name="update_admin"),
    path('delete_admin/<admin_id>/', views.delete_admin, name="delete_admin"),
    path('add_admin/', views.add_admin, name="add_admin"),
    
  
]