from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.appName("CSVReadWriteExample").getOrCreate()

# Define the schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# Create sample data
data = [("Alice", 25, "New York"), ("Bob", 30, "London"), ("Charlie", 35, "Paris")]

# Create a DataFrame with the schema
df = spark.createDataFrame(data, schema)

# Write the DataFrame to a CSV file
df.write.csv("people.csv")

# Stop the SparkSession
spark.stop()



#READ the CSV file

# Define the schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# Read the CSV file with the specified schema
df = spark.read.csv("people.csv", header=True, schema=schema)

# Show the DataFrame contents
df.show()

# Stop the SparkSession
spark.stop()
