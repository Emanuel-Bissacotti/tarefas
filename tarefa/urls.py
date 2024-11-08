from django.urls import path

from .views import TarefaListView, TarefaCreateView, TarefaUpdateView, TarefaDeleteView

urlpatterns = [
    path('listar', TarefaListView.as_view(), name='tarefa_list'),
    path('cadastrar', TarefaCreateView.as_view(), name='tarefa_create'),
    path('alterar/<int:pk>', TarefaUpdateView.as_view(), name='tarefa_update'),
    path('apagar/<int:pk>', TarefaDeleteView.as_view(), name='tarefa_delete'),
]