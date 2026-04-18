# AWS Credit Card Fraud ETL Pipeline

An end-to-end AWS ETL pipeline that automatically processes incoming credit card transaction files and stores cleaned output for fraud analysis.

---

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
- Amazon Athena
- PySpark
- Visual Studio Code

---

## AWS Services Used

- Amazon S3 → Store raw and processed transaction files
- AWS Lambda → Automatically trigger the ETL process
- AWS Glue → Clean and transform transaction data
- AWS IAM → Manage access and permissions
- AWS CloudWatch → Monitor logs and execution
- Amazon Athena → Query processed fraud data using SQL

---

## Project Workflow

1. Upload `fraudTrain.csv` or `fraudTest.csv` into the raw S3 bucket:

    fraud-raw-data-274588776541/incoming/

2. Amazon S3 automatically triggers the AWS Lambda function:

    trigger_glue_job

3. Lambda receives the uploaded file path and starts the AWS Glue job:

    fraud-cleaning-job

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


## Key Features
--Fully automated ETL pipeline
--Event-driven architecture
--Processes only the newly uploaded file
--Creates a custom risk_level column
--Stores processed train and test data separately
--Built using real-world AWS services


## Athena SQL Analysis

The processed fraud transaction data was queried using Amazon Athena.

Sample business queries performed:

--Count of HIGH vs LOW risk transactions
--Top states with highest fraud activity
--Top merchants with the highest transaction count
--Fraud vs Non-Fraud transaction comparison
--Top transaction categories

SQL files available in:

athena/create_table.sql
athena/fraud_analysis_queries.sql

Athena screenshots available in:

athena/screenshots/risk-level-query.png
athena/screenshots/top-states-query.png
athena/screenshots/top-merchants-query.png
athena/screenshots/fraud-vs-nonfraud-query.png
athena/screenshots/top-categories-query.png

## Power BI Dashboard

A dashboard was created in Microsoft Power BI using the processed fraud transaction data exported from Amazon Athena.

Dashboard Name:

Credit Card Fraud Analytics Dashboard

The dashboard includes:

- HIGH vs LOW risk transactions
- Fraud vs Non-Fraud transaction count
- Top 10 fraud states
- Top 10 merchants by transaction count
- Top transaction categories
- KPI cards for total transactions and fraud activity

Power BI files available in:

powerBI/credit_fraud_dashboard.pbix

Dashboard screenshots available in:

screenshots/


## Future Improvements
--Build a Power BI dashboard using processed data
--Add SNS alerts for high-risk transactions
--Build a machine learning model for fraud prediction
--Automatically archive processed raw files
--Add data partitioning for better Athena performance



##Folder Structure
credit-card-fraud-pipeline/
│
├── athena/
│   ├── create_table.sql
│   ├── fraud_analysis_queries.sql
│   └── screenshots/
│       ├── risk-level-query.png
│       ├── top-states-query.png
│       ├── top-merchants-query.png
│       ├── fraud-vs-nonfraud-query.png
│       └── top-categories-query.png
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
├── powerBI/
│   ├── fraud_dashboard.pbix
│   ├── Risk level summary.csv
│   ├── Top 10 merchants with the highest number of transactions.csv
│   ├── Top 10 states with highest number of transactions.csv
│   ├── Top 10 transaction categories.csv
│   └── Fraud_vs_non-fraud.csv
│
├── screenshots/
│   ├── Buckets_create.png
│   ├── Raw data Folder.png
│   ├── Raw data save.png
│   ├── lambda_trigger.png
│   ├── Fraud_cleaning_job_scripts.png
│   ├── ETL job running.png
│   ├── processed data folder.png
│   ├── ETL_output_data.png
│   ├── dashboard-overview.png
│   ├── risk-level-visual.png
│   ├── top-states-visual.png
│   └── top-merchants-visual.png
│
├── .gitignore
└── README.md