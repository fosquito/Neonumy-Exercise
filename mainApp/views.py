from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from .models import Image

class ListImage(ListView):
    model = Image
  
class CreateImage(CreateView):
    model = Image
    fields = ['img']
    success_url = reverse_lazy('image_list')

class DetailImage(DetailView):
    model = Image
    
class DeleteImage(DeleteView):
    model = Image
    success_url = reverse_lazy('image_list')