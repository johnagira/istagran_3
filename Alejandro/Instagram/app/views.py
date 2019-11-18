from django.shortcuts import render, redirect
from .models import User, Pub, Follow

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        informacion = User.objects.filter(username=request.POST['username'], password=request.POST['password']).exists()

        if informacion is True:
            obtener = User.objects.get(username=request.POST['username'], password=request.POST['password'])
            request.session['login'] = 1
            request.session['user_id'] = obtener.id
            
            return redirect('noticias')
        else:
            return render(request, 'home.html', {'error' : 'Credenciales invalidas'})
    else:
        if(request.session.get('login') == 1):
            return redirect('noticias')
        else:
            return render(request, 'home.html')
            
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        usuario = User.objects.filter(username=request.POST['username']).exists()
        if usuario is True:
            return render(request, 'registro.html', {'error' : 'El usuario ya existe.'})
        else:
            correo = User.objects.filter(email=request.POST['correo']).exists()
            if correo is True:
                return render(request, 'registro.html', {'error' : 'El correo ya existe.'})
            else:
                crear = User.objects.create(username=request.POST['username'], email=request.POST['correo'], nombre=request.POST['nombre'], password=request.POST['password'])
                request.session['login'] = 1
                request.session['user_id'] = crear.id
                
                return redirect('noticias')
    else:
        if(request.session.get('login') == 1):
            return redirect('noticias')
        else:
            return render(request, 'registro.html')

    return render(request, 'registro.html')

def noticias(request):
    if request.method == 'GET':
        if(request.session.get('login') != 1):
            return redirect('home')
        else:
            publicaciones = Pub.objects.all()
            
            try:
                seguidores = Follow.objects.get(id_usuario=request.session['user_id'])
                return render(request, 'noticias.html', {'seguidores':seguidores, 'publicaciones':publicaciones})
            except Follow.DoesNotExist:
                return render(request, 'noticias.html')
                
    return render(request, 'noticias.html')

def perfil(request):
    if request.method == 'GET':
        publicaciones = Pub.objects.filter(id_usuario=request.session['user_id'])
        usuarios = User.objects.filter(id_usuario=request.session['user_id'])
        total_publicaciones = Pub.objects.filter(id_usuario=request.session['user_id']).count()
        total_seguidos = Follow.objects.filter(id_usuario=request.session['user_id']).count()
        total_seguidores = Follow.objects.filter(id_usuario_seguido=request.session['user_id']).count()
        
        return render(request, 'perfil.html', {'publicaciones':publicaciones, 'usuarios':usuarios, 'total_publicaciones':total_publicaciones, 'total_seguidos':total_seguidos, 'total_seguidores':total_seguidores})
    else:
        usuario = User.objects.get(username=request.POST['search'])
    
        publicaciones = Pub.objects.filter(id_usuario=usuario.id)
        usuarios = User.objects.filter(id=usuario.id)
        total_publicaciones = Pub.objects.filter(id_usuario=usuario.id).count()
        total_seguidos = Follow.objects.filter(id_usuario=usuario.id).count()
        total_seguidores = Follow.objects.filter(id_usuario_seguido=usuario.id).count()
        
        try:
            seguidor = Follow.objects.get(id_usuario=request.session['user_id'], id_usuario_seguido=usuario.id)
            
            return render(request, 'perfil.html', {'publicaciones':publicaciones, 'usuarios':usuarios, 'total_publicaciones':total_publicaciones, 'total_seguidos':total_seguidos, 'total_seguidores':total_seguidores, 'seguidor':seguidor})
        except Follow.DoesNotExist:
            return render(request, 'perfil.html', {'publicaciones':publicaciones, 'usuarios':usuarios, 'total_publicaciones':total_publicaciones, 'total_seguidos':total_seguidos, 'total_seguidores':total_seguidores})

def logout(request):
    del request.session['login']
    del request.session['user_id']
    return render(request, 'home.html')