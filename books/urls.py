from django.urls import path
from . import views

urlpatterns = [
    # Form-based URLs
    path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('admin/', views.admin_book_list, name='admin_book_list'),
    path('admin/create/', views.admin_book_create, name='admin_book_create'),
    path('admin/<int:pk>/update/', views.admin_book_update, name='admin_book_update'),
    path('admin/<int:pk>/delete/', views.admin_book_delete, name='admin_book_delete'),
    # API URLs
    path('api/books/', views.BookListAPI.as_view(), name='api_book_list'),
    path('api/books/<int:pk>/', views.BookDetailAPI.as_view(), name='api_book_detail'),
    path('api/cart/', views.CartAPI.as_view(), name='api_cart'),
    path('api/cart/<int:item_id>/', views.CartItemAPI.as_view(), name='api_cart_item'),
    path('api/orders/', views.OrderAPI.as_view(), name='api_order'),
]