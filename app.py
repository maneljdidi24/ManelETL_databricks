from pyspark.sql import SparkSession

print("START SPARK")

spark = SparkSession.builder \
    .appName("ETL Test") \
    .master("local[*]") \
    .getOrCreate()

df = spark.createDataFrame(
    [(1, "Alice"), (2, "Bob"), (3, "suzy")],
    ["id", "name"]
)

df.show()

spark.stop()
print("END SPARK")
print("CD TEST OK 🚀")
print("okj")


