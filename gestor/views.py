from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Formulario de Registro
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import GroupForm, ActaCongresoForm, RevistaCientificaForm, InformeTecnicoForm, ArticuloForm, AutorForm
from .models import Group_Invest, Acta_congreso, Revista_cientifica, Informe_tecnico, Articulo, Autor
from datetime import date
# Create your views here.

def gestor(request):
    return render(request, 'gestor.html')

@login_required
def home(request):
    try:
        groups = Group_Invest.objects.all()
        articles = Articulo.objects.all()
        return render(request, 'home.html', {'groups': groups, 'articles': articles})
    except Exception as e:
        return render(request, 'home.html', {'error': f'Error al recuperar datos: {str(e)}'})

def signup(request):
    
    if request.method == 'GET':
         return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
           try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save() #guarda el ususario en el modelo
                login(request, user)
                return redirect('home')
           except IntegrityError:
               return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'Nombre de usuario o contraseña incorrectos'})
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm} )
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm, 'error': 'Nombre de usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')
        
@login_required 
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.save()
            return redirect('home')
        else:
            return render(request, 'create_group.html', {
                'form': form,  # Pasar la instancia del formulario en caso de error
                'error': 'Por favor, proporcione información válida'
            })
    else:
        form = GroupForm()  # Crear una instancia vacía del formulario
        return render(request, 'create_group.html', {
            'form': form  # Pasar la instancia vacía del formulario
        })
            
def create_acta_congreso(request):
    if request.method == 'POST':
        form = ActaCongresoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o a donde sea necesario
    else:
        form = ActaCongresoForm()
    return render(request, 'create_acta_congreso.html', {'form': form})

def update_acta_congreso(request, pk):
    acta_congreso = get_object_or_404(Acta_congreso, pk=pk)
    if request.method == 'POST':
        form = ActaCongresoForm(request.POST, instance=acta_congreso)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o a donde sea necesario
    else:
        form = ActaCongresoForm(instance=acta_congreso)
    return render(request, 'update_acta_congreso.html', {'form': form})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.save()
            return redirect('tipo articulos')
        else:
            return render(request, 'create_article.html', {
                'form': form,  # Pasar la instancia del formulario en caso de error
                'error': 'Por favor, proporcione información válida'
            })
    else:
        form = ArticuloForm()  # Crear una instancia vacía del formulario
        return render(request, 'create_article.html', {
            'form': form  # Pasar la instancia vacía del formulario
        })


def create_autor(request, group_id):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_detail')
    else:
        form = AutorForm()

    return render(request, 'create_autor.html', {'form': form})

def calcular_edad(fecha_nacimiento):
    today = date.today()
    return today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            
def group_detail(request, group_id):
    group = get_object_or_404(Group_Invest, id=group_id)
    articles = Articulo.objects.filter(id_autor__id_grupo=group)  # Si tienes relación con artículos
    context = {
        'group': group,
        'articles': articles,
    }
    return render(request, 'group_detail.html', context)

def article(request, article_id):
    article = get_object_or_404(Articulo, id=article_id)
    autor = article.id_autor # Si tienes relación con artículos
    grupo = autor.id_grupo
    # Calcular la edad del autor
    edad_autor = calcular_edad(autor.fecha_nac)
    context = {
        'autor': autor,
        'article': article,
        'grupo': grupo,
        'edad_autor': edad_autor,
    }
    return render(request, 'article.html', context)