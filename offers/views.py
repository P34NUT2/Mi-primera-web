from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy 
from .models import Offer
from .forms import OfferForm
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect


#para acceder al modelo de User
User = get_user_model()

class OfferCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    form_class = OfferForm
    template_name = 'offers/offer_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task_id = self.kwargs['task_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks')  #cambiar mas adelante si es posible o ponerle un if para que confirme que fue succes 

#modelo tipo list para las listas de tareas 
class MyOffersView(LoginRequiredMixin, ListView):
    model = Offer
    template_name = 'offers/my_offers.html'
    context_object_name = 'offers'

    '''dejar la oferta tipo tarjeta como en personas que an ofertado y arreglar el detalle  '''
    def get_queryset(self):
        return Offer.objects.filter(user=self.request.user).select_related('task').order_by('-created_at')

#para el futuro por si lanzo esto cambiar oh hacer algo para que no sea insegura esta vista
class OffersReceivedView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'offers/received.html'
    context_object_name = 'tasks'

    '''para manana en clase poner bonito los botones de perfil y ademas arreglar un boton con el task detail'''
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).prefetch_related('offers')





class OfferStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Offer
    fields = []  # no se muestran campos, solo se actualiza status desde la vista
    template_name = 'offers/offer_status_update.html'
    context_object_name = 'offer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = self.kwargs.get('action')  # 👉 ahora estará disponible en el template
        return context

    def get(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.task.author != request.user:
            messages.error(request, "No tienes permiso para modificar esta oferta.")
            return redirect('offers_received')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        action = self.kwargs.get('action')

        if action == 'accept':
            form.instance.status = 'accepted'
            messages.success(self.request, "Oferta aceptada.")
        elif action == 'reject':
            form.instance.status = 'rejected'
            messages.success(self.request, "Oferta rechazada.")
        else:
            messages.error(self.request, "Acción no válida.")
            return redirect('tasks')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks')

