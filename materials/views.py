from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')
    template_name = 'materials/material_form.html'


class MaterialListView(ListView):
    model = Material
    template_name = 'materials/material_list.html'


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/material_detail.html'
