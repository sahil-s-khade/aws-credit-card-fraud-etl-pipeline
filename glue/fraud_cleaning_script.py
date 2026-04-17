import sys
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

args = getResolvedOptions(sys.argv, ['input_path'])

spark = SparkSession.builder.appName("FraudCleaningJob").getOrCreate()

df = spark.read.option("header", "true").csv(args['input_path'])

df = df.dropDuplicates()
df = df.dropna()

df = df.withColumn("amt", col("amt").cast("double"))

df = df.withColumn(
    "risk_level",
    when(col("amt") > 20000, "HIGH").otherwise("LOW")
)

output_folder = "test" if "fraudTest" in args['input_path'] else "train"

df.coalesce(1).write.mode("append").option("header", "true").csv(
    f"s3://fraud-processed-data-274588776541/cleaned/{output_folder}/"
)