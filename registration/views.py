from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from tasks.models import Task
from .models import Profile
from django.urls import reverse_lazy
from .forms import UserRegisterForm, ProfileForm

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        profile = self.request.user.profile

        # Si el perfil está vacío o incompleto (puedes ajustar esto como gustes)
        if not profile.full_name or not profile.university:
            return reverse_lazy('profile-edit') + '?first-time'
        # Si ya tiene perfil completo, redirige al home
        return reverse_lazy('home') + '?login'


#clases para el perfil
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_edit.html'  
    success_url = reverse_lazy('home')  # cambiar a futuro por el la misma vista al perfil publico

    def get_object(self):
        return self.request.user.profile

class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile_detail.html'


#arreglar el slugify bien puesto para la url, el context ver si sobra y que pase los paramteros en clase y los objetos
#del usurio para que pueda aggarrar solo esos obejtos eh instancias y los muestre en html en el template
class ProfileTaskView(ListView):
    model = Task
    template_name = 'registration/profile_public_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = User.objects.filter(username=username).first()
        return Task.objects.filter(author=user).exclude(offers__status='accepted').order_by('-created_at') if user else Task.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_name'] = User.objects.get(username=self.kwargs['username'])
        return context

#clase para que se pueda ver el perfil publico 
class PublicProfileView(DetailView):
    model = User
    template_name = 'registration/profile_public.html'
    context_object_name = 'profile_user'# nombre que quiera usar obvio se basa en el modelo user
    #estos dos son importantes por que el kwarg busca en la url y el field  busca el username en el modelo
    slug_field = 'username'
    slug_url_kwarg = 'username'