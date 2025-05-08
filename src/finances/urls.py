from django.urls import path
from . import views
from finances.views import TransactionListView, TransactionCreateFormView

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('new/', TransactionCreateFormView.as_view(), name='transaction_create'),
]