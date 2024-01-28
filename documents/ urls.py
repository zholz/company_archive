from django.urls import path
from .views import DocumentListView, DocumentDetailView, DocumentCreateView, DocumentUpdateView, DocumentDeleteView

urlpatterns = [
    path('', DocumentListView.as_view(), name='document_list'),
    path('document/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('document/new/', DocumentCreateView.as_view(), name='document_new'),
    path('document/<int:pk>/edit/', DocumentUpdateView.as_view(), name='document_edit'),
    path('document/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),
]
