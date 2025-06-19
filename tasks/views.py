from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy

#NOTA: El objet context es como llamare mi objeto en mi template
#NOTA:Slug lo puse como slug jsjsj para no perderme
#Nota puedo hacer los mixins en un mixin.py pero asi esta bien  por ahora 

#para el misxin que segun la docuemntacion sirve para que alguien que no este logeado accede a alas tarea y las borre y las cambie


#Esta clase sirve para listar todas las tareas por asi decirlo 
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "tasks/task_list.html"
    
    def get_queryset(self):
            return Task.objects.exclude(offers__status='accepted').order_by('-created_at')

#Esta para que un usuario cree tarea OJO:DEBO DE CAMBIARLA DESPUES PARA RELACIONAR MODELOS 
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#Para ver toda la tarea y con los detalles en grande
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()

        user_offer = None
        if self.request.user.is_authenticated:
            has_offered = task.offers.filter(user=self.request.user).exists()
            user_offer = task.offers.filter(user=self.request.user).first()
        else:
            has_offered = False

        context['has_offered'] = has_offered
        context['user_offer'] = user_offer
        return context


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'  
    success_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return (
            self.request.user == task.author or 
            self.request.user.is_staff or  
            self.request.user.is_superuser
        )


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

    #funcion del mixin para que pueda editar borrar etc
    def test_func(self):
        task = self.get_object()
        return (
            self.request.user == task.author or 
            self.request.user.is_staff or 
            self.request.user.is_superuser
        )


"""lo siguiente es hacer para que se pueda pedir una tarea y la barra de mensajes para completar la tarea """