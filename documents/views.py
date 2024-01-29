from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from django.core.paginator import Paginator

class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
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
