from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('', views.gestor, name='gestor'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_group/', views.create_group, name='create group'),
    path('create_article/', views.create_article, name='create_article'),
    path('grupo/<int:group_id>/', views.group_detail, name='group_detail'),
    path('create_autor/', views.create_autor, name='crear_autor'),
    path('grupo/<int:group_id>/create_autor/', views.create_autor, name='create_autor'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('article/<int:id>/edit/', views.article_detail, name='edit_article'),
    path('article/<int:id>/delete/', views.delete_article, name='delete_article'),
    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),
    #path('type_article/', views.type_article, name='tipo articulo'),
    path('tabla/', views.tabla, name='tabla'),
    path('list_articles/', views.list_articles, name='lista articulos'),
]

