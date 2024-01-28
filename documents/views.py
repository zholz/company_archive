from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document

class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'document_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'document_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document_confirm_delete.html'
    context_object_name = 'document'
    success_url = reverse_lazy('document_list')
