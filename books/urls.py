from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/order/', views.place_order, name='place_order'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('book/<int:pk>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/place-order/', views.place_order_from_cart, name='place_order_from_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/increase/<int:pk>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', views.decrease_quantity, name='decrease_quantity'),

    path('order-success/', views.order_success, name='order_success'),
    path('reset-cart/', views.reset_cart, name='reset_cart'),

    # ✅ Admin Panel (Custom)
    path('admin-panel/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('admin-panel/book/<int:pk>/edit/', views.update_book_price, name='update_book_price'),
    path('admin-panel/book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('admin-panel/book/add/', views.add_book, name='add_book'),

    # ✅ Export routes with correct names
    path('export-books/', views.export_books_csv, name='export_books'),  # Matches {% url 'export_books' %}
    path('export-filtered/', views.export_filtered_books_csv, name='export_filtered_books'),  # Matches {% url 'export_filtered_books' %}
    # Custom admin views for cards
    path('admin-users/', views.admin_user_list, name='admin_user_list'),
    path('admin-orders/', views.admin_order_list, name='admin_order_list'),
    path('admin-books/', views.admin_book_list, name='admin_book_list'),
    
]
