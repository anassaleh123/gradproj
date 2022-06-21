from django.urls import path
from . import views
urlpatterns = [
    path('',views.getRoutes),
    path('danger/', views.getDanger),
    path('danger/create/', views.createDanger),
    path('danger/<str:pk>/update/', views.updateDanger),
    path('danger/<str:pk>/delete/', views.deleteDanger),
    path('danger/<str:pk>/', views.getDanger0),
    path('dangermlmodel/', views.mlmodel),
   

]