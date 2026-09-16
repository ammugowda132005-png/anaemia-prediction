from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('result/<str:prediction>/', views.result, name='result'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line
    path('about/', views.about, name='about'),
    path('data_analytics/', views.data_analytics, name='data_analytics'),

]
