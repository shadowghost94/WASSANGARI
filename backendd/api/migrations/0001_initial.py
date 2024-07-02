# Generated by Django 5.0 on 2024-06-26 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Divinite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Ethnie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("langue", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Evenement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date", models.DateField()),
                ("lieu", models.CharField(max_length=255)),
                ("statut", models.CharField(max_length=55)),
                ("nbr_places_dispo", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Monument",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("localisation", models.CharField(max_length=255)),
                ("date_inauguration", models.DateField()),
                ("nom_concepteur", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
                ("visiteurs_annuels", models.IntegerField()),
                ("horaires", models.CharField(max_length=255)),
                ("prix_entree", models.DecimalField(decimal_places=2, max_digits=10)),
                ("organisme_gestion", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Musee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("localisation", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("superficie", models.FloatField()),
                ("prix_entree", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_fondation", models.DateField()),
                ("type_musee", models.CharField(max_length=255)),
                ("visiteurs_annuels", models.IntegerField()),
                ("horaires", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ParcNational",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("localisation", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("visiteurs_annuels", models.IntegerField()),
                ("organisme_gestion", models.CharField(max_length=255)),
                ("superficie", models.FloatField()),
                ("horaires", models.CharField(max_length=255)),
                ("prix_entree", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Reserve",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("localisation", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("visiteurs_annuels", models.IntegerField()),
                ("organisme_gestion", models.CharField(max_length=255)),
                ("superficie", models.FloatField()),
                ("horaires", models.CharField(max_length=255)),
                ("prix_entree", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="SiteHistorique",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("localisation", models.CharField(max_length=255)),
                ("date_classement", models.DateField()),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
                ("visiteurs_annuels", models.IntegerField()),
                ("horaires", models.CharField(max_length=255)),
                ("prix_entree", models.DecimalField(decimal_places=2, max_digits=10)),
                ("organisme_gestion", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ObjetExpose",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("origine", models.CharField(max_length=255)),
                ("date_appartenance", models.CharField(max_length=255)),
                (
                    "musee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.musee"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EspeceArbre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom_scientifique", models.CharField(max_length=255)),
                ("nom_commun", models.CharField(max_length=255)),
                ("reserves", models.ManyToManyField(blank=True, to="api.reserve")),
            ],
        ),
        migrations.CreateModel(
            name="EspeceAnimal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom_scientifique", models.CharField(max_length=255)),
                ("nom_commun", models.CharField(max_length=255)),
                (
                    "parcs_nationaux",
                    models.ManyToManyField(blank=True, to="api.parcnational"),
                ),
                ("reserves", models.ManyToManyField(blank=True, to="api.reserve")),
            ],
        ),
        migrations.CreateModel(
            name="Royaume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
                (
                    "ethnie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ethnie"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContenuMultimedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("image", "Image"),
                            ("video", "Video"),
                            ("audio", "Audio"),
                        ],
                        max_length=10,
                    ),
                ),
                ("media_url", models.CharField(max_length=255)),
                (
                    "monument",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.monument",
                    ),
                ),
                (
                    "musee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.musee",
                    ),
                ),
                (
                    "parc_national",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.parcnational",
                    ),
                ),
                (
                    "reserve",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.reserve",
                    ),
                ),
                (
                    "site_historique",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.sitehistorique",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tradition",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("histoire", models.TextField()),
                (
                    "ethnie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ethnie"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Utilisateur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("prenom", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("pays", models.CharField(max_length=255)),
                ("ville", models.CharField(max_length=255)),
                ("date_naissance", models.DateField()),
                ("premium", models.BooleanField(default=False)),
                ("numero_momo", models.CharField(blank=True, max_length=255)),
                ("num_carte_paiement", models.CharField(blank=True, max_length=255)),
                (
                    "media_profil_url",
                    models.ImageField(default="default.jpg", upload_to="user_images"),
                ),
                ("sexe", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("password", models.CharField(max_length=255)),
                ("verified", models.BooleanField(default=False)),
                (
                    "ethnie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.ethnie"
                    ),
                ),
                (
                    "monuments_visites",
                    models.ManyToManyField(blank=True, to="api.monument"),
                ),
                ("musees_visites", models.ManyToManyField(blank=True, to="api.musee")),
                (
                    "parcs_visites",
                    models.ManyToManyField(blank=True, to="api.parcnational"),
                ),
                (
                    "reserves_visites",
                    models.ManyToManyField(blank=True, to="api.reserve"),
                ),
                (
                    "sites_visites",
                    models.ManyToManyField(blank=True, to="api.sitehistorique"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "evenement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.evenement"
                    ),
                ),
                (
                    "utilisateur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.utilisateur",
                    ),
                ),
            ],
        ),
    ]
