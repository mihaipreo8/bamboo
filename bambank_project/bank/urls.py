from django.urls import path
from .views import (
	TransactionListView, 
	TransactionDetailView,
	TransactionCreateView,
	UserTransactionListView
)
from . import views

urlpatterns = [
    path('', TransactionListView.as_view() , name='bank-home'),
    path('user/<str:username>', UserTransactionListView.as_view(), name='user-transactions'),
    path('transaction/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transaction/new/', TransactionCreateView.as_view(), name='transaction-create'),
    path('about/', views.about, name='bank-about'),

]