from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create sample data
data = [["John", 30, "12345"], ["Jane", 25, "54321"], ["Mike", 40, "98765"]]

# Create a DataFrame
df = spark.createDataFrame(data, ["name", "age", "id"])

# Select multiple columns by name
df_selected1 = df.select("name", "age")
df_selected1.show()

# Select columns by position
df_selected2 = df.select(df.columns[0], df.columns[1])
df_selected2.show()

# Select columns using the `col` function
df_selected3 = df.select(col("name"), col("id"))
df_selected3.show()
