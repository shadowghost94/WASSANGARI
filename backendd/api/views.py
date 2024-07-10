from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string 
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect
from api.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from backendd.settings import *
from django.contrib.auth.hashers import check_password, make_password

from django.core.mail import send_mail, EmailMessage
from .token import generatorToken

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user':user})

@login_required
def apprendre(request):
    user = request.user
    return render(request, 'apprendre.html', {'user':user})

@login_required
def decouvrir(request):
    user = request.user
    return render(request, 'decouvrir.html', {'user':user})

@login_required
def visiter(request):
    user = request.user
    return render(request, 'visiter.html', {'user':user})

@login_required
def explorer(request):
    user = request.user
    return render(request, 'explorer.html', {'user':user})

@login_required
def informer(request):
    user = request.user
    return render(request, 'informer.html', {'user':user})

@login_required
def acheter(request):
    user = request.user
    return render(request, 'acheter.html', {'user':user})

@login_required
def evenement(request):
    user = request.user
    return render(request, 'evenements.html', {'user':user})

@csrf_exempt
@login_required
def modifierProfil(request):
    if request.method == "POST":
        user = request.user
        user.nom = request.POST.get('nom', user.nom)
        user.prenom = request.POST.get('prenom', user.prenom)
        user.email = request.POST.get('email', user.email)
        
        current_password = request.POST.get('password', '')
        new_password = request.POST.get('password-confirm', '')

        if check_password(current_password, user.password):
            user.set_password(new_password)
            user.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Mot de passe actuel incorrect'})
    else:
        return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})

#Vue de connexion
def connexion(request, comment=None):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        
        user = authenticate(email=email, password=password)
       
        try:
            my_user = Utilisateur.objects.get(email=email)
        except Utilisateur.DoesNotExist:
            my_user = None

        if user is not None:
            login(request, user)
            return dashboard(request)
        
        elif my_user is not None and not my_user.is_active:
            comment ="Vous n'avez pas confirmé votre adresse e-mail. Veuillez confirmer votre adresse e-mail avant de réessayer à nouveau !"
            return render(request, 'connexion.html', {'comment':comment})

        else:
            comment = "E-mail ou mot de passe incorrect. Veuillez réessayer !"
            return render(request, 'connexion.html', {'comment': comment})
    
    return render(request, 'connexion.html', {'comment': comment})

#Vue d'inscription
def inscription(request, comment=None):
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        sexe = request.POST['sexe']
        ethnie_id = request.POST['ethnie']
        password = request.POST['password']
        password1 = request.POST['password-confirm']
        media_profil = request.FILES['photo_profil']

        if Utilisateur.objects.filter(email=email):
            messages.error(request, "Veuillez utiliser une autre adresse e-mail")
            return redirect('inscription')
        
        if password != password1:
            messages.error(request, "Vous avez entré deux mots de passes différents")

        mon_utilisateur = Utilisateur(nom=nom, prenom=prenom, email=email, media_profil_url=media_profil, sexe=sexe, ethnie=ethnie_id, password=make_password(password))

        try:
            mon_utilisateur.save()
        except:
            messages.error(request, "Une erreur s'est produite. Veuillez réssayer !")
            return redirect('connexion')

        messages.success(request, "Votre compte a été crée avec succès, veuillez consulter votre adresse e-mail pour valider")
        
        #Envoie du premier email de bienvenue
        subject = "E-mail de bienvenue"
        message = f"""
                Bonjour {mon_utilisateur.prenom} {mon_utilisateur.nom},

                Nous sommes ravis de vous accueillir sur Wassangari, la plateforme dédiée à la découverte et à la promotion des cultures béninoises.

                Votre compte a été créé avec succès. Avant de vous connecter, veuillez visiter le deuxième mail envoyé afin de confirmer votre e-mail

                Nous vous invitons à explorer les nombreuses fonctionnalités de notre plateforme :
                - Découvrez les sites historiques, monuments, parcs nationaux, réserves et musées.
                - Apprenez-en plus sur les différentes ethnies, traditions et divinités du Bénin.
                - Participez aux événements culturels et réservez vos tickets en ligne.
                - Et bien plus encore !

                Nous espérons que vous apprécierez votre expérience sur Wassangari et que vous trouverez de nombreuses opportunités pour enrichir vos connaissances et votre appréciation des cultures béninoises.

                Si vous avez des questions ou avez besoin d'assistance, n'hésitez pas à nous contacter à support@wassangari.com.

                Encore une fois, bienvenue et merci de nous rejoindre !

                Cordialement,
                L'équipe Wassangari
            """
        from_email = EMAIL_HOST_USER

        to_list = [mon_utilisateur.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)

        #Email de confirmation
        current_site = get_current_site(request)
        email_subject = "Confirmation de votre adresse e-mail sur la plateforme Wassangari"
        messageConfirm = render_to_string("emailconfirm.html", {
            "name": mon_utilisateur.nom,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(mon_utilisateur.pk)),
            "token": generatorToken.make_token(mon_utilisateur),
        })
        email = EmailMessage(
            email_subject,
            messageConfirm,
            EMAIL_HOST_USER,
            [mon_utilisateur.email]
        )

        email.fail_silently = False
        email.send()
        comment ="Votre compte a été créer veuillez consulter vos mails pour valider !"
        return inscription(request, comment)
    
    ethnies = Ethnie.objects.all()
    return render(request, 'inscription.html', {'ethnies': ethnies})

#fonction d'activation d'email
def activate(request, uidb64, token):
    try:
        uid = str(urlsafe_base64_decode(uidb64), encoding='utf-8')
        user = Utilisateur.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Utilisateur.DoesNotExist):
        user = None

    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Félicitation, votre compte a bien été activé !")
        return redirect('connexion')
    else:
        messages.error(request, "La confirmation a échoué")
        return redirect('index')
    
def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez bien été déconecté')
    return redirect('index')