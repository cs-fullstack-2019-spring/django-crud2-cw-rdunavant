from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users/create/<int:id>', views.createuser, name='create'),
    path('users/read/<int:id>', views.readuser, name='read'),
    path('users/update/<int:id>', views.updateuser, name='update'),
    path('users/delete/<int:id>', views.deleteuser, name='delete'),
]