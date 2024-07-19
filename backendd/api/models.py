from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Royaume(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)

    def __str__(self):
        return self.nom

class Ethnies(models.Model):
    nom = models.CharField(max_length=255)
    langue = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField()
    royaume = models.ForeignKey(Royaume, on_delete=models.DO_NOTHING)

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

class Chant_Danse(models.Model):
    TYPE_CHOICES = [
        ('chant', 'Chants'),
        ('danse', 'Danses'),
    ]
    titre = models.CharField(max_length=55)
    auteur = models.CharField(max_length=55)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)
    ethnie = models.ForeignKey(Ethnies, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.titre
    
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
    chant_danse = models.ForeignKey(Chant_Danse, on_delete=models.DO_NOTHING, null=True, blank=True)

class UtilisateurManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email est requis.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Utilisation de make_password n'est pas nécessaire ici
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    sexe = models.CharField(max_length=10)
    ethnie_id = models.CharField(max_length=255, null=True, blank=True)
    premium = models.BooleanField(default=False)
    numero_momo = models.CharField(max_length=255, null=True, blank=True)
    num_carte_paiement = models.CharField(max_length=255, null=True, blank=True)
    media_profil_url = models.ImageField(upload_to='photos_profil/', null=True, blank=True)
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
    is_staff = models.BooleanField(default=False)  # Ajout du champ is_staff
    is_superuser = models.BooleanField(default=False)  # Ajout du champ is_superuser

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

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

class ObjetVente(models.Model):
    titre = models.CharField(max_length=64)
    auteur = models.CharField(max_length=64)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    media_url = models.ImageField(upload_to='photo_objetVente/', null=True, blank=True, default='photo_objetVente/default.jpg')

class Actualites(models.Model):
    titre = models.CharField(max_length=255)
    contenue = models.TextField()
    media_url = models.ImageField(upload_to='photo_actualites/', null=True, blank=True, default='photo_actualites/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    prix_entree = models.DecimalField(max_digits=10, decimal_places=2)
    nbr_places_dispo = models.IntegerField()
    media_profil_url = models.ImageField(upload_to='photo_evenement/', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.nom

class Ticket(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Tradition(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)
    ethnie = models.ForeignKey(Ethnies, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nom

class Divinite(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField(null=True)

    def __str__(self):
        return self.nom
    
#jared@gmail.com
#jareddenver