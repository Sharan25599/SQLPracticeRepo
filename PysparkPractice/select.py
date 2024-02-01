from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Create a DataFrame
data = [["John", 30, "12345"], ["Jane", 25, "54321"], ["Mike", 40, "98765"]]
df = spark.createDataFrame(data, ["name", "age", "id"])

# Select the "name" column
df_name = df.select("name")

# Show the selected column
df_name.show()



