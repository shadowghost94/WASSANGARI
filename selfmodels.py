from django.db import models
    
class SiteHistorique(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    date_classement = models.DateField()
    description = models.TextField()
    histoire = models.TextField()
    visiteurs_annuel = models.IntegerField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.CharField(max_length=55)
    organism_gestion = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    
class Monument(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    date_inauguration = models.DateField()
    nom_concepteur = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField()
    visiteurs_annuel = models.IntegerField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.CharField(max_length=55)
    organism_gestion = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class ParcNational(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    visiteurs_annuel = models.IntegerField()
    organism_gestion = models.CharField(max_length=255)
    superficie = models.FloatField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.CharField(max_length=55)

    def __str__(self):
        return self.nom

class Reserve(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    visiteurs_annuel = models.IntegerField()
    organism_gestion = models.CharField(max_length=255)
    superficie = models.FloatField()
    horaires = models.CharField(max_length=255)
    prix_entree = models.CharField(max_length=55)

    def __str__(self):
        return self.nom
    
class Musee(models.Model):
    nom = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    description = models.TextField()
    superficie = models.FloatField()
    prix_entree = models.CharField(max_length=55)
    date_fondation = models.DateField()
    type_musee = models.CharField(max_length=255)
    visiteurs_annuel = models.IntegerField()
    horaires = models.CharField(max_length=255)

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
    site_historique_id = models.IntegerField(default=0)
    monument_id = models.IntegerField(default=0)
    parc_national_id = models.IntegerField(default=0)
    reserve_id = models.IntegerField(default=0)
    musee_id = models.IntegerField(default=0)
    ethnie_id = models.IntegerField(default=0)
    espece_animal_id = models.IntegerField(default=0)
    espece_arbre_id = models.IntegerField(default=0)
    royaume_id = models.IntegerField(default=0)
    tradition_id = models.IntegerField(default=0)
    divinite_id = models.IntegerField(default=0)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pays = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    ethnie_id = models.IntegerField()
    date_naissance = models.DateField()
    premium = models.BooleanField(default=False)
    media_profil_url = models.ImageField(default="default.jpg", upload_to="user_images")
    sexe = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=50)
    sites_visites = models.ManyToManyField(SiteHistorique, on_delete=models.DO_NOTHING)
    monuments_visites = models.ManyToManyField(Monument, on_delete=models.DO_NOTHING)
    parcs_visites = models.ManyToManyField(ParcNational, on_delete=models.DO_NOTHING)
    reserve_visites = models.ManyToManyField(Reserve, on_delete=models.DO_NOTHING)
    musee_visites = models.ManyToManyField(Musee, on_delete=models.DO_NOTHING)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Ethnie(models.Model):
    nom = models.CharField(max_length=255)
    langue = models.CharField(max_length=255)
    description = models.TextField()
    histoire = models.TextField()
    users = models.ManyToManyField(Utilisateur)
    
class Premium(Utilisateur):
    numero_momo = models.CharField(max_length=255)
    num_carte_paiement = models.CharField(max_length=255)

    class Meta:
        proxy = True 

class Objets_exposes(models.Model):
    nom_objet = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    origine = models.CharField(max_length=55)
    date_appartenance = models.CharField(max_length=55)
    musee = models.ForeignKey(Musee)

class Espece_Arbre(models.Model):
    nom_scientifique = models.CharField(max_length=55)
    nom_commun = models.CharField(max_length=55)
    reserve = models.ManyToManyField(Reserve)

class Espece_animal(models.Model):
    nom_scientifique = models.CharField(max_length=55)
    nom_commun = models.CharField(max_length=55)
    parc_national = models.ManyToManyField(ParcNational)
    reserve = models.ManyToManyField(Reserve)

class Evenement(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.CharField(max_length=55)
    lieu = models.CharField(max_length=255)
    statut = models.CharField(max_length=55)
    nbr_place_dispo = models.IntegerField()

class Ticket(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.DO_NOTHING)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING)

class Royaume(models.Model):
    nom = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    histoire = models.TextField()
    ethnie = models.ForeignKey(Ethnie, on_delete=models.DO_NOTHING)

class Tradition(models.Model):
    nom = models.CharField(max_length=155)
    description = models.CharField(max_length=255)
    histoire = models.TextField()
    ethnie = models.ForeignKey(Ethnie, on_delete=models.DO_NOTHING)

class Divinite(models.Model):
    nom = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    histoire = models.TextField()
