from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Formulario de Registro
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import GroupForm, ActaCongresoForm, RevistaCientificaForm, InformeTecnicoForm, ArticuloForm, AutorForm
from .models import Group_Invest, Acta_congreso, Revista_cientifica, Informe_tecnico, Articulo, Autor, Tipo_articulo
from datetime import date
from django.db.models import Q

# Create your views here.

# Helper functions
def calcular_edad(fecha_nacimiento):
    today = date.today()
    return today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

#Interfaces de inicio
def gestor(request):
    return render(request, 'gestor.html')

@login_required
def home(request):
    try:
        search_by = request.GET.get('search_by')
        query = request.GET.get('q')
        
        groups = Group_Invest.objects.all()
        articles = Articulo.objects.all()
        
        if query:
            if search_by == 'titulo':
                articles = articles.filter(titulo__icontains=query)
            elif search_by == 'autor':
                articles = articles.filter(id_autor__nombre__icontains=query)
            elif search_by == 'palabras_clave':
                articles = articles.filter(palabras_clave__icontains=query)
            elif search_by == 'tipo':
                articles = articles.filter(id_tipo__tipo__icontains=query)
            elif search_by == 'ubicacion':
                articles = articles.filter(ubicacion__icontains=query)
        
        return render(request, 'home.html', {'groups': groups, 'articles': articles})
    except Exception as e:
        return render(request, 'home.html', {'error': f'Error al recuperar datos: {str(e)}'})

# Autenticación
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

# Vistas de Grupo
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

@login_required            
def group_detail(request, group_id):
    group = get_object_or_404(Group_Invest, id=group_id)
    articles = Articulo.objects.filter(id_autor__id_grupo=group)  # Si tienes relación con artículos
    autores = Autor.objects.filter(id_grupo=group_id)
    context = {
        'group': group,
        'articles': articles,
        'autores': autores
    }
    return render(request, 'group_detail.html', context)

def delete_group(request, id):
    group = get_object_or_404(Group_Invest, id = id)
    group.delete()
    return redirect('home')

# Vistas de Artículos
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.save()
            return redirect('tipo articulos', id=new_article.id)
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

def article(request, article_id):
    article = get_object_or_404(Articulo.objects.select_related('id_autor', 'id_tipo'), id=article_id)
    actas = Acta_congreso.objects.filter(id_articulo=article_id)
    informes = Informe_tecnico.objects.all()
    for info in informes:
         if info.id_articulo_id == article_id:
             print('si')

    revistas = Revista_cientifica.objects.filter(id_articulo_id=article_id)  # Cambia revista por revistas en plural
    autor = article.id_autor
    grupo = autor.id_grupo
    
    # Calcular la edad del autor
    edad_autor = calcular_edad(autor.fecha_nac)
    
    # Verificar si el artículo es de tipo Informe Técnico
    tipo_de_articulo = article.id_tipo.id
    print(tipo_de_articulo)
    
    context = {
        'autor': autor,
        'article': article,
        'grupo': grupo,
        'edad_autor': edad_autor,
        'tipo_de_articulo': tipo_de_articulo,
        'informes': informes,
        'actas': actas,
        'revistas': revistas  # Asegúrate de que el nombre aquí coincida con el que usas en la plantilla
    }
    return render(request, 'article.html', context)

@login_required
def article_detail(request, id):
    article = get_object_or_404(Articulo, id=id)

    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'article_detail.html', {'article': article, 'form': form, 'error': 'Error al actualizar el artículo'})
    else:
        form = ArticuloForm(instance=article)
        return render(request, 'article_detail.html', {'article': article, 'form': form})

@login_required
def delete_article(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    articulo.delete()
    return redirect('tabla')

@login_required
def type_article(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    id_tipo = articulo.id_tipo.tipo  # Obtén el valor del tipo del artículo
    
    if id_tipo == 'Informe Técnico':
        if request.method == 'GET':
            form = InformeTecnicoForm(initial={'id_articulo': id})
            return render(request, 'type_article.html', {'form': form, 'articulo': articulo})
        else:
            form = InformeTecnicoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')  # Redirige a la página de inicio
    elif id_tipo == 'Acta de Congreso':
        if request.method == 'GET':
            form = ActaCongresoForm(initial={'id_articulo': id})
            return render(request, 'type_article.html', {'form': form, 'articulo': articulo})
        else:
            form = ActaCongresoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        if request.method == 'GET':
            form = RevistaCientificaForm(initial={'id_articulo': id})
            return render(request, 'type_article.html', {'form': form, 'articulo': articulo})
        else:
            form = RevistaCientificaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')


# Vistas de Autor
@login_required
def create_autor(request, group_id):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()

    return render(request, 'create_autor.html', {'form': form})

@login_required            
def autor(request, autorContent):
    # Aquí puedes obtener el autor a partir de su nombre
    # Por ejemplo, si estás buscando en la base de datos, sería algo como:
    autor = Autor.objects.filter(nombre=autorContent).first()  # Puedes ajustar esto para obtener el autor
    if not autor:
        return HttpResponse('Autor no encontrado', status=404)

    # Supongamos que tienes artículos que mostrar del autor
    articles = Articulo.objects.filter(id_autor=autor.id)
    edad = calcular_edad(autor.fecha_nac)
    # Renderizar los artículos en una plantilla
    return render(request, 'autor.html', {'autor': autor, 'articles': articles, 'edad': edad})

@login_required
def search_suggestions(request):
    query = request.GET.get('q', '')
    search_by = request.GET.get('search_by', 'titulo')  # Por defecto buscar por título
    
    if search_by == 'autor':
        results = Autor.objects.filter(nombre__icontains=query).values_list('nombre', flat=True)
    elif search_by == 'palabras_clave':
        results = Articulo.objects.filter(palabras_clave__icontains=query).values_list('palabras_clave', flat=True)
    elif search_by == 'tipo':
        results = Articulo.objects.filter(id_tipo__tipo__icontains=query).values_list('id_tipo__tipo', flat=True)
    elif search_by == 'ubicacion':
        results = Articulo.objects.filter(ubicacion__icontains=query).values_list('ubicacion', flat=True)
    else:
        results = Articulo.objects.filter(titulo__icontains=query).values_list('titulo', flat=True)
    
    suggestions = list(set(results))  # Eliminar duplicados
    
    return JsonResponse({'suggestions': suggestions})

@login_required
def tabla(request):
    return render(request, 'tabla.html')

def list_articles(request):
    articulos = Articulo.objects.select_related('id_autor').values(
        'id', 'titulo', 'palabras_clave', 'copia', 'ubicacion', 'id_autor__nombre', 'id_tipo_id'
    )
    data = {'articulos': list(articulos)}
    return JsonResponse(data)

@login_required
def group(request, id):
    group = get_object_or_404(Group_Invest, id=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('tabla')
        else:
            return render(request, 'group.html', {'group': group, 'form': form, 'error': 'Error al actualizar el artículo'})
    else:
        form = GroupForm(instance=group)
        return render(request, 'group.html', {'group': group, 'form': form})

@login_required
def autor_detail(request, id):
    autor = get_object_or_404(Autor, id=id)
    edad = calcular_edad(autor.fecha_nac)
    articles = Articulo.objects.filter(id_autor=autor)
    return render(request, 'autor.html', {'autor': autor, 'edad': edad, 'articles': articles})

@login_required
def delete_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.delete()
    return redirect('home')

def ubicacion(request, ubicacion):
    articles = Articulo.objects.filter(ubicacion = ubicacion)
    return render(request, 'ubicacion.html', {'articles': articles, 'ubicacion': ubicacion})