from django.urls import path
from . import views
urlpatterns = [
    
    path('list_faq/', views.list_faq, name="list_admin"),
    path('add_faq/', views.add_faq, name="add_admin"),
    
  
]