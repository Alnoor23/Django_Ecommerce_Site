from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.store, name='store'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('product/<int:id>', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('updateitem/', views.updateItem, name='updateitem'),
    path('checkout/', views.checkout, name='checkout'),
    path('processorder/', views.processsOrder, name='process_order'),
    path('workingonitmaybe/', views.Build, name='build'),
]