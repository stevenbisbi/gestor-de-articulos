from django.urls import path
from gestor import views

urlpatterns = [
    path('', views.gestor, name='gestor'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    #Grupos
    path('create_group/', views.create_group, name='create group'),
    path('grupo/<int:group_id>/', views.group_detail, name='group_detail'),
    path('grupo/<int:id>/edit', views.group, name='grupo'),
    path('grupo/<int:id>/delete', views.delete_group, name='delete_group'),
    path('grupo/<int:group_id>/create_autor/', views.create_autor, name='create_autor'),
    #Articulos
    path('create_article/', views.create_article, name='create_article'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('article/<int:id>/edit/', views.article_detail, name='edit_article'),
    path('article/<int:id>/delete/', views.delete_article, name='delete_article'),
    #Tipo de articulos
    path('type_article/<int:id>', views.type_article, name='tipo articulos'),
    #Autores
    path('create_autor/', views.create_autor, name='crear_autor'),
    path('autor/<str:autorContent>/', views.autor, name= 'autor'),
    path('autor/<int:id>/edit', views.autor_detail, name= 'autor'),
    path('autor/<int:id>/delete', views.delete_autor, name= 'autor'),
    #Ubicación
    path('ubicacion/<str:ubicacion>/', views.ubicacion, name= 'ubicacion'),
    #JavaScript
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
    path('tabla/', views.tabla, name='tabla'),
    path('list_articles/', views.list_articles, name='lista articulos'),
]

