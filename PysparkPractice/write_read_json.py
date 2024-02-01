# Writing a JSON File

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.appName("JSONSchemaExample").getOrCreate()

# Define the schema
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# Create sample data
data = [("Alice", 25, "New York"), ("Bob", 30, "Los Angeles")]

# Create a DataFrame
df = spark.createDataFrame(data, schema)

# Write the DataFrame to a JSON file
df.write.json("people.json")

# Stop the SparkSession
spark.stop()


# Reading the JSON File

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.appName("JSONSchemaExample").getOrCreate()

# Define the schema (same as the one used for writing)
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# Read the JSON file into a DataFrame using the schema
df = spark.read.json("people.json", schema=schema)

# Print the DataFrame contents
df.show()

# Stop the SparkSession
spark.stop()

# Read Muti_line JSON file

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.appName("MultiLineJSONExample").getOrCreate()

# Define the schema (if applicable)
schema = StructType([
    # ... define your schema fields here
])

# Read the multi-line JSON file with schema (optional)
df = spark.read.json("multiline.json", multiline=True, schema=schema)

# Process the DataFrame
df.show()

# Stop the SparkSession
spark.stop()

