from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistroForm
from django.urls import reverse_lazy
from .models import Usuario

# Vista para el inicio de sesión
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') # Redirección a la página de inicio después del inicio de sesión
        else:
            messages.error(request, 'Usuario o contraseña inválido, intente de nuevo')
    
    return render(request, 'usuarios/login.html')

# Vista para el cierre de sesión
def user_logout(request):
    logout(request)
    return redirect('login')


# Vista para el registro de usuarios
class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'

def form_valid(self, form):
    response = super().form_valid(form)
    user = self.object
    # Crear un usuario con rol "Miembro" al registrarse
    Usuario.objects.create(user=user, tipo_usuario=Usuario.USUARIO_MIEMBRO)
    return response