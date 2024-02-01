from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.getOrCreate()

# Data with a nested column "address" containing "street" and "city"
data = [
    ("Alice", {"street": "1st Street", "city": "New York"}),
    ("Bob", {"street": "Main Street", "city": "London"})
]

df = spark.createDataFrame(data, ["name", "address"])

# Rename nested column "street" to "new_street" using dot notation
df_renamed = df.withColumnRenamed("address.street", "address.new_street")

df_renamed.show()
