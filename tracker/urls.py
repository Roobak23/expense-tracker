from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add'),
    path('edit/<int:id>/', views.edit_expense, name='edit'),
    path('delete/<int:id>/', views.delete_expense, name='delete'),
]
