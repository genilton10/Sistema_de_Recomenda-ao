from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    #Pre-processamento
	path('stopwords', views.rm_stopwords, name='rm_stopwords'),
    path('stemmer', views.aplic_stemmer, name='aplic_stemmer'),
    path('palavras', views.busc_palavras, name='busc_palavras'),
    path('palavrasunicas', views.busc_palavras_unicas, name='busc_palavras_unicas'),
    path('frequencia', views.busc_frequencia, name='busc_frequencia'),
    #Metrica
    path('matriz', views.matriz_confusao, name='matriz_confusao'),
    path('accuracy', views.accuracy, name='accuracy'),

   	#Classe
   	path('classe', views.classe_list, name='classe_list'),
    path('classe/<int:pk>/', views.classe_detail, name='classe_detail'),
    path('classe/new', views.classe_new, name='classe_new'),
    path('classe/<int:pk>/edit/', views.classe_edit, name='classe_edit'),
   	path('classe/<pk>/remove/', views.classe_remove, name='classe_remove'),
]