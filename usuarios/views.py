from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro (request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')