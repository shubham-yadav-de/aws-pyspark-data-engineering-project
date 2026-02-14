from pyspark.sql.functions import col

# Remove records with null amount
clean_df = df.filter(col("amount").isNotNull())
