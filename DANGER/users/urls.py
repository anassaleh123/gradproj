from django.urls import path
from . import views
urlpatterns = [
   
    path('list_user/', views.list_user, name="list_user"),
    path('update_user/<user_id>/', views.update_user, name="update_user"),
    path('delete_user/<user_id>/', views.delete_user, name="delete_user"),
    path('add_user/', views.add_user, name="add_user")

]