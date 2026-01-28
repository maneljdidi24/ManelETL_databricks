# etl_notebook_csv.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1️⃣ Créer la SparkSession
spark = (
    SparkSession.builder
    .appName("ManelETL_CSV")
    .master("local[*]")  # Exécution locale
    .getOrCreate()
)

print("✅ SparkSession créée")

# 2️⃣ Lire le fichier CSV source
input_path = "data/input.csv"  # chemin vers ton fichier source
df = spark.read.csv(input_path, header=True, inferSchema=True)

print("✅ Fichier CSV lu")
df.show(5)

# 3️⃣ Nettoyage / transformation des données
# Exemple : supprimer les lignes avec des valeurs nulles
df_clean = df.dropna()

# Exemple : filtrer une colonne spécifique (si besoin)
# df_clean = df_clean.filter(col("colonne_exemple") != "")

print("✅ Nettoyage terminé")
df_clean.show(5)

# 4️⃣ Écrire le DataFrame en CSV
output_path = "data/output_csv"  # dossier de sortie
df_clean.coalesce(1).write.mode("overwrite").csv(output_path, header=True)

print(f"✅ ETL terminé, CSV généré dans : {output_path}")

# 5️⃣ Lecture rapide pour vérifier
df_result = spark.read.csv(output_path, header=True, inferSchema=True)
df_result.show(5)
