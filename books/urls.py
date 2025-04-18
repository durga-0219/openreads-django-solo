from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/order/', views.place_order, name='place_order'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # ✅ Use your custom login view!
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('book/<int:pk>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/place-order/', views.place_order_from_cart, name='place_order_from_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),

    path('order-success/', views.order_success, name='order_success'),
    path('reset-cart/', views.reset_cart, name='reset_cart'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # ✅ only keep once
]
