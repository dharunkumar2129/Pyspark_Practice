from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Load").master("local[*]").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True).csv("AAT.csv")

df.show()
df.printSchema()
print(df.columns)
