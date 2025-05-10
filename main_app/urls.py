from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('stores/', views.store_index, name='store-index'),
    path('stores/<int:store_id>/', views.store_detail, name='store-detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='store-create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='store-update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='store-delete'),
    
    path('pieces/create/', views.PieceCreate.as_view(), name='piece-create'),
    path('pieces/<int:pk>/', views.PieceDetail.as_view(), name='piece-detail'),
    path('pieces/', views.PieceList.as_view(), name='piece-index'),
    path('pieces/<int:pk>/update/', views.PieceUpdate.as_view(), name='piece-update'),
    path('pieces/<int:pk>/delete/', views.PieceDelete.as_view(), name='piece-delete'),

    path('stores/<int:store_id>/associate-piece/<int:piece_id>/', views.associate_piece, name='associate-piece'),
    path('stores/<int:store_id>/remove-piece/<int:piece_id>/', views.remove_piece, name='remove-piece'),

    path('accounts/signup/', views.signup, name='signup'),
]