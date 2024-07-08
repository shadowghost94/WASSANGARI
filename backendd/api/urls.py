from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('dashboard/', views.dashboard, name="dashboard"),
     path('apprendre/', views.apprendre, name="apprendre"),
     path('decouvrir/', views.decouvrir, name="decouvrir"),
     path('visiter/', views.visiter, name="visiter"),
     path('explorer/', views.explorer, name="explorer"),
     path('informer/', views.informer, name="informer"),
     path('acheter/', views.acheter, name="acheter"),
     path('evenements/', views.evenement, name="evenements"),
     path('connexion/', views.connexion, name ='connexion'),
     path('deconnexion/', views.deconnexion, name='deconnexion'),
     path('inscription/', views.inscription, name ='inscription'),
     path('activate/<uidb64>/<token>', views.activate, name="activate"),
     path('modifierProfil/', views.modifierProfil, name="modifierProfil"),
]