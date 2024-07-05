from django.contrib import admin
from api.models import (
    SiteHistorique, Monument, ParcNational, Reserve, Musee,
    ContenuMultimedia, Utilisateur, Ethnie, ObjetExpose,
    EspeceArbre, EspeceAnimal, Evenement, Ticket, Royaume,
    Tradition, Divinite, Chant_Danse
)

class SiteHistoriqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation', 'date_classement', 'visiteurs_annuels')
    search_fields = ('nom', 'localisation')
    list_filter = ('date_classement', 'localisation')

class MonumentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation', 'date_inauguration', 'visiteurs_annuels')
    search_fields = ('nom', 'localisation')
    list_filter = ('date_inauguration', 'localisation')

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email','sexe', 'ethnie', 'premium', 'verified')
    search_fields = ('nom', 'prenom', 'email', 'pays', 'ville')
    list_filter = ('premium', 'verified')

# Enregistrement des modèles avec les personnalisations
admin.site.register(SiteHistorique, SiteHistoriqueAdmin)
admin.site.register(Monument, MonumentAdmin)
admin.site.register(ParcNational)
admin.site.register(Reserve)
admin.site.register(Musee)
admin.site.register(ContenuMultimedia)
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Ethnie)
admin.site.register(ObjetExpose)
admin.site.register(EspeceArbre)
admin.site.register(EspeceAnimal)
admin.site.register(Evenement)
admin.site.register(Ticket)
admin.site.register(Royaume)
admin.site.register(Tradition)
admin.site.register(Divinite)
admin.site.register(Chant_Danse)