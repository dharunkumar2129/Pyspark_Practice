from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Dharun").master("local[*]").getOrCreate()
print(spark.version)