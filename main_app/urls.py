from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('stores/', views.store_index, name='store-index'),
    
    path('accounts/signup/', views.signup, name='signup'),
]
