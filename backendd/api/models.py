from django.db import models
from django.contrib.auth.models import AbstractUser

class Ethnie(models.Model):
    nom = models.CharField(max_length=255)
    langue = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField()

    def __str__(self):
        return self.nom

class SiteHistorique(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    date_classement = models.DateField()
    description = models.TextField()
    histoire = models.TextField(null=True)
    visiteurs_annuels = models.IntegerField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)
    organisme_gestion = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Monument(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    date_inauguration = models.DateField()
    nom_concepteur = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)
    visiteurs_annuels = models.IntegerField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)
    organisme_gestion = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class ParcNational(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    visiteurs_annuels = models.IntegerField()
    organisme_gestion = models.CharField(max_length=255)
    superficie = models.FloatField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Reserve(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    visiteurs_annuels = models.IntegerField()
    organisme_gestion = models.CharField(max_length=255)
    superficie = models.FloatField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Musee(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    superficie = models.FloatField()
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)
    date_fondation = models.DateField()
    type_musee = models.CharField(max_length=255)
    visiteurs_annuels = models.IntegerField()
    horaires = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Chant(models.Model):
    titre = models.CharField(max_length=55)
    auteur = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    ethnie = models.ForeignKey(Ethnie, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titre

class Danse(models.Model):
    nom = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    ethnie = models.ForeignKey(Ethnie, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nom
    
class ContenuMultimedia(models.Model):
    TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    media_url = models.CharField(max_length=255)
    site_historique = models.ForeignKey(SiteHistorique, on_delete=models.DO_NOTHING, null=True, blank=True)
    monument = models.ForeignKey(Monument, on_delete=models.DO_NOTHING, null=True, blank=True)
    parc_national = models.ForeignKey(ParcNational, on_delete=models.DO_NOTHING, null=True, blank=True)
    reserve = models.ForeignKey(Reserve, on_delete=models.DO_NOTHING, null=True, blank=True)
    musee = models.ForeignKey(Musee, on_delete=models.DO_NOTHING, null=True, blank=True)
    chant = models.ForeignKey(Chant, on_delete=models.DO_NOTHING, null=True, blank=True)
    danse = models.ForeignKey(Danse, on_delete=models.DO_NOTHING, null=True, blank=True)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sexe = models.CharField(max_length=10)
    ethnie = models.IntegerField(null=True, blank=True)
    premium = models.BooleanField(default=False)
    numero_momo = models.CharField(max_length=255, null=True, blank=True)
    num_carte_paiement = models.CharField(max_length=255, null=True, blank=True)
    media_profil_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    sites_visites = models.ManyToManyField(SiteHistorique)
    monuments_visites = models.ManyToManyField(Monument)
    parcs_visites = models.ManyToManyField(ParcNational)
    reserves_visites = models.ManyToManyField(Reserve)
    musees_visites = models.ManyToManyField(Musee)
    verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class ObjetExpose(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    origine = models.CharField(max_length=255)
    date_appartenance = models.CharField(max_length=255)
    musee = models.ForeignKey(Musee, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class EspeceArbre(models.Model):
    nom_scientifique = models.CharField(max_length=255)
    nom_commun = models.CharField(max_length=255)
    reserves = models.ManyToManyField(Reserve, blank=True)

    def __str__(self):
        return self.nom_commun

class EspeceAnimal(models.Model):
    nom_scientifique = models.CharField(max_length=255)
    nom_commun = models.CharField(max_length=255)
    parcs_nationaux = models.ManyToManyField(ParcNational, blank=True)
    reserves = models.ManyToManyField(Reserve, blank=True)

    def __str__(self):
        return self.nom_commun

class Evenement(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    lieu = models.CharField(max_length=255)
    statut = models.CharField(max_length=55)
    nbr_places_dispo = models.IntegerField()

    def __str__(self):
        return self.nom

class Ticket(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Royaume(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)
    ethnie = models.ForeignKey(Ethnie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Tradition(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)
    ethnie = models.ForeignKey(Ethnie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Divinite(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)

    def __str__(self):
        return self.nom