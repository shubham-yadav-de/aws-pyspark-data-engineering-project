# Write processed data to output location
clean_df.write.mode("overwrite").parquet("data/processed/")
