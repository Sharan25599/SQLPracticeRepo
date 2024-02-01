from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample DataFrame
data = [("James", 25, "M"), ("Alice", 30, "F"), ("Robert", 42, "M")]
df = spark.createDataFrame(data, ["name", "age", "gender"])

# Drop the "gender" column
df_dropped = df.drop("gender")

# Display the DataFrame to verify
df_dropped.show()

# Drop the "age" column
df_without_age = df.drop("age")

# Drop the "gender" column from the new DataFrame
df_without_age_gender = df_without_age.drop("gender")

# Display the DataFrame to verify
df_without_age_gender.show()

