from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from backendd import info

def index(request):
    return render(request, 'index.html')

def apprendre(request):
    return render(request, 'apprendre.html')

def decouvrir(request):
    return render(request, 'decouvrir.html')

def visiter(request):
    return render(request, 'visiter.html')

def explorer(request):
    return render(request, 'explorer.html')

def informer(request):
    return render(request, 'informer.html')

def acheter(request):
    return render(request, 'acheter.html')

def evenement(request):
    return render(request, 'evenements.html')

def connexion(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            name = user.nom+' '+user.prenom
            
            return render(request, 'app/index.html', {'name':name})
        else:
            messages.error(request, "Mauvaise authentification")
            return redirect('connection')
        
    return render(request, 'connexion.html')

def inscription(request):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        sexe = request.POST['sexe']
        ethnie = request.POST['ethnie']
        password = request.POST['password']
        password1 = request.POST['password-confirm']

        if Utilisateur.objects.filter(email=email):
            messages.error(request, "Veuillez une autre adresse e-mail")
            return redirect('inscription')
        
        if password != password1:
            messages.error(request, "Vous avez entré deux mots de passes différents")

        mon_utilisateur = Utilisateur.objects.create_user(nom, prenom, email, sexe, ethnie, password )
        mon_utilisateur.save()

        messages.success(request, "Votre compte a été crée avec succès, veuillez consulter votre adresse e-mail pour valider")
        subject = "Bienvenue !"
        message = "Bienvenue sur la plateforme Wassangari "
        from_email = info.EMAIL_HOST_USER
        to_list = [mon_utilisateur.email]
        return redirect('connexion')
    
    return render(request, 'inscription.html')