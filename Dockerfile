FROM python:3.11-slim

# Installer Java
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Variables d'environnement
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=python

# Dossier de travail
WORKDIR /app

# Copier les dépendances
COPY Requirements.txt .

# Installer les libs Python
RUN pip install --no-cache-dir -r Requirements.txt

# Copier le code
COPY app.py .

# Commande par défaut
CMD ["python", "app.py"]
