# AWS Credit Card Fraud ETL Pipeline

An end-to-end AWS ETL pipeline that automatically processes incoming credit card transaction files and stores cleaned output for fraud analysis.

## Project Overview

This project simulates a real-world banking fraud detection workflow using AWS cloud services. When a new CSV transaction file is uploaded into Amazon S3, the system automatically triggers an ETL process using AWS Lambda and AWS Glue.

The ETL pipeline:
- Detects newly uploaded transaction files
- Cleans and transforms the data
- Identifies high-risk transactions
- Stores processed output in separate train and test folders

---

## Technologies Used

- Python
- AWS S3
- AWS Lambda
- AWS Glue
- AWS IAM
- AWS CloudWatch
- PySpark
- Visual Studio Code

---

## AWS Services Used

- Amazon S3 → Store raw and processed transaction files
- AWS Lambda → Automatically trigger the ETL process
- AWS Glue → Clean and transform transaction data
- AWS IAM → Manage access and permissions
- AWS CloudWatch → Monitor logs and execution

---

## Project Workflow

1. Upload `fraudTrain.csv` or `fraudTest.csv` into the raw S3 bucket:

   `fraud-raw-data-274588776541/incoming/`

2. Amazon S3 automatically triggers the AWS Lambda function:

   `trigger_glue_job`

3. Lambda receives the uploaded file path and starts the AWS Glue job:

   `fraud-cleaning-job`

4. AWS Glue processes only the newly uploaded file.

5. The ETL script performs the following transformations:
   - Removes duplicate rows
   - Removes null values
   - Converts the `amt` column into numeric format
   - Creates a `risk_level` column

```python
df = df.dropDuplicates()
df = df.dropna()

df = df.withColumn("amt", col("amt").cast("double"))

df = df.withColumn(
    "risk_level",
    when(col("amt") > 20000, "HIGH").otherwise("LOW")
)

6.Transactions with amount greater than 20,000 are marked as HIGH risk.

7.Processed output is automatically saved into:
fraud-processed-data-274588776541/cleaned/train/
fraud-processed-data-274588776541/cleaned/test/

##Project structure
aws-credit-card-fraud-etl-pipeline/
│
├── data/
│   └── sample_transactions.csv
│
├── glue/
│   └── fraud_cleaning_script.py
│
├── lambda/
│   └── trigger_glue_job.py
│
├── screenshots/
│   ├── Buckets_create.png
│   ├── lambda_trigger.png
│   ├── ETL job running.png
│   ├── ETL_output_data.png
│   └── processed data folder.png
│
└── README.md


Key Features
#Fully automated ETL pipeline
#Event-driven architecture
#Processes only the newly uploaded file
#Creates a custom risk_level column
#Stores processed train and test data separately
#Built using real-world AWS services


Sample Output
#cleaned/train/ → processed fraudTrain data
#cleaned/test/ → processed fraudTest data


Future Improvements
1.Add Amazon Athena for SQL-based fraud analysis
2.Build a Power BI dashboard using processed data
3.Add SNS alerts for high-risk transactions
4.Build a machine learning model for fraud prediction
5.Automatically archive processed raw files