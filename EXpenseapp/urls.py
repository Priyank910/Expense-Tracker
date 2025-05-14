from django.urls import path
from pkg_resources.extern import names

from . import views

urlpatterns = [
    path('', views.index),
    path('add_expense', views.add_expense),
    path('all-expenses', views.all_expenses),
    path('/delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]