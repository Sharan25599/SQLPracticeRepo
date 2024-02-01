from Pyspark.sql import SparkSession
from Pyspark.sql.functions import lit

spark=SparkSession.builder.appName("AddColumn").getOrCreate()

# Create a sample DataFrame
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 27)
]

columns = ["name", "age"]
df = SparkSession.createDataFrame(data, columns)


# Add a new column called "city" with a constant value
df_with_new_column = df.withColumn("city", lit("Bangalore"))

# Update the "age" column by adding 1
df_updated = df_with_new_column.withColumn("age", df_with_new_column.age + 1)

df_updated.show()