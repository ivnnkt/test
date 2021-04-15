from django.urls import path
from . import views


urlpatterns = [
    path('wallets/', views.WalletListView.as_view(), name='wallets'),
    path('wallets/<int:pk>/', views.WalletDetailView.as_view(), name='wallet_detail'),
    path('wallets/<int:pk>/edit', views.WalletUpdaitView.as_view(), name='wallet_edit'),
    path('wallets/<int:pk>/delete', views.WalletDeleteView.as_view(), name='wallet_del'),
    path('wallets/add', views.WalletCreateView.as_view(), name='wallet_add'),
    path('transactions/', views.TransactionListView.as_view(), name='transactions'),
    path('transactions/add', views.TransactionCreateView.as_view(), name='transaction_add'),
    path('transactions/<int:pk>/delete', views.TransactionDeleteView.as_view(), name='transaction_del'),
]
