from django.shortcuts import render, redirect
from .models import User

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        informacion = User.objects.filter(username=request.POST['username'], password=request.POST['password']).exists()

        if informacion is True:
            request.session['username'] = request.POST['username']
            return redirect('noticias')
        else:
            return render(request, 'home.html', {'error' : 'Credenciales invalidas'})
    return render(request, 'home.html')

def registro(request):
    return render(request, 'registro.html')

def noticias(request):
    return render(request, 'noticias.html')