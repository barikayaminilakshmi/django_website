from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('detail/<int:id>/', views.product_detail, name='detail'),

    path('admin-products/', views.admin_products, name='admin_products'),

    path('add/', views.add_product, name='add'),

    path('update/<int:id>/', views.update_product, name='update'),

    path('delete/<int:id>/', views.delete_product, name='delete'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

]