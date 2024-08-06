WASSANGARI

Wassangari est une plateforme d'éducation culturelle et artistique. L'objectif de la plateforme est de fournie aux utilisateurs une immersio complète dans la culture béninoise en leur offrant un accès facile à des informations détaillées sur l'histoire les traditions, les coutumes, langues, les chants/danses, ...

SOMMAIRE
    Installation
    Configuration
    Utilisation
    Tests
    Déploiement
    Contribuer

Installation
Prérequis

Assurez-vous que vous avez les outils suivants installés :

    Python 3.x
    pip (pour installer les dépendances Python)
    virtualenv (optionnel mais recommandé pour les environnements virtuels)

Cloner le dépôt

bash

git clone https://github.com/Shadowghost94/WASSANGARI.git
cd WASSANGARI

Créer et activer un environnement virtuel

bash

python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`

Installer les dépendances

bash

pip install -r requirements.txt

Configuration clé de settings.py avec utilisation de mysql par défaut:

SECRET_KEY = "django-insecure-5tkne!-vjoi7h0!#p-3m$kkmojev63p=$!3%r*o2tix=mcbnqw"
DJANGO_DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "wassangari",
        "USER": "phpmyadmin",
        "PASSWORD": "admin",
        "HOST": "localhost"
    }
}

Configurer la base de données

Si vous utilisez PostgreSQL, vous devez configurer la base de données dans settings.py et appliquer les migrations :

bash

python manage.py migrate

Utilisation
Démarrer le serveur de développement

Pour démarrer le serveur de développement, utilisez la commande suivante :

bash

python manage.py runserver

Vous pouvez maintenant accéder à l'application en allant sur http://127.0.0.1:8000/ dans votre navigateur.
Créer un super utilisateur

Pour accéder à l'interface d'administration Django, vous devez créer un super utilisateur :

bash

python manage.py createsuperuser

Tests

Pour exécuter les tests unitaires de votre application, utilisez :

bash

python manage.py test

Déploiement
Préparer le déploiement

Assurez-vous que les variables d'environnement sont correctement configurées et que vous avez effectué les migrations nécessaires.
Déploiement sur Heroku

Si vous déployez sur Heroku, assurez-vous d'avoir installé Heroku CLI. Voici les étapes :

    Se connecter à Heroku :

    bash

heroku login

Créer une nouvelle application Heroku :

bash

heroku create

Déployer sur Heroku :

bash

git push heroku main

Appliquer les migrations :

bash

heroku run python manage.py migrate

Créer un super utilisateur (optionnel) :

bash

    heroku run python manage.py createsuperuser

## Propriété Intellectuelle

Ce projet est la propriété intellectuelle de Waxangari L@bs. Toute copie, distribution, ou utilisation de ce projet sans autorisation écrite explicite de Waxangari l@bs est interdite.

Pour toute demande d'autorisation ou de renseignements supplémentaires, veuillez contacter waxangarilabs@gmail.com.


