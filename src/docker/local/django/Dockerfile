# Étape 1 : Utilisation de l'image Python pour construire les dépendances
ARG PYTHON_VERSION=3.11.8-bullseye

FROM python:${PYTHON_VERSION} as python

# Étape 2 : Construction des dépendances
FROM python as python-build-stage

# Définition de l'environnement de construction (ici, local)
ARG BUILD_ENVIRONMENT=local



# Mise à jour des paquets et installation des outils de construction
#Méta-paquet pour les outils de compilation de base
# Fichiers de développement pour PostgreSQL
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \  
    libpq-dev

# Copie des fichiers requirements.txt dans le conteneur
COPY ./requirements .

# Installation des dépendances Python via pip et création des wheels
RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt  

# Étape 3 : Exécution de l'application
FROM python as python-run-stage

# Définition de l'environnement de construction (ici, local)
ARG BUILD_ENVIRONMENT=local

# Définition du répertoire de travail
ARG APP_HOME=/app 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}
WORKDIR ${APP_HOME}

# Installation des paquets nécessaires (identique à l'étape précédente)
# Bibliothèque pour la localisation et la traduction   gettext  
# Nettoyage des paquets inutilisés
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \ 
    && rm -rf /var/lib/apt/lists/* 

# Copie des wheels depuis l'étape de construction précédente
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Installation des dépendances Python à partir des wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# Copie des scripts d'entrée et attribution des permissions d'exécution
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

# Copie du code de l'application dans le conteneur
COPY . ${APP_HOME}

# Définition de l'entrée principale pour l'exécution du conteneur
ENTRYPOINT [ "/entrypoint" ]
