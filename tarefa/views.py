from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Tarefa

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefa/tarefa_list.html'
    context_object_name = 'tarefas'

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ['categoria', 'descricao', 'obs', 'realizada']
    template_name = 'tarefa/tarefa_form.html'
    success_url = reverse_lazy('tarefa_list')

class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ['categoria', 'descricao', 'obs', 'realizada']
    template_name = 'tarefa/tarefa_form.html'
    success_url = reverse_lazy('tarefa_list')

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'tarefa/tarefa_confirm_delete.html'
    success_url = reverse_lazy('tarefa_list')