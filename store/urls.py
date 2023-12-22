from django.urls import path
from .views import school_supply, add_supply,dashboard,edit_supply, delete_supply, supply_detail, signup_view, login_view, logout_view

urlpatterns = [
   path('', school_supply, name='school_supply'),
    path('school_supply/add/', add_supply, name='add_supply'),
    path('dashboard/', dashboard, name='dashboard'),
    path('school_supply/edit/<int:pk>/', edit_supply, name='edit_supply'),
    path('dashboard/delete/<int:pk>/', delete_supply, name='delete_supply'),
    path('products/<int:pk>/', supply_detail, name='supply_detail'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
