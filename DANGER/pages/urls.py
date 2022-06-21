from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-bracelet', views.add_bracelet, name='add-bracelet'),
    path('add-acc', views.add_acc, name='add-acc'),
    path('add-faq', views.add_faq, name='add-faq'),
    path('add-users', views.add_users, name='add-users'),
    path('add', views.add, name='add'),
    path('show', views.show, name='show'),
    path('show-bracelet', views.show_bracelet, name='show-bracelet'),
    path('show-acc', views.show_acc, name='show-acc'),
    path('show-faq', views.show_faq, name='show-faq'),
    path('show-users', views.show_users, name='show-users'),
]