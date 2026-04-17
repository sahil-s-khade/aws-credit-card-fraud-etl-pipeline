import boto3

glue = boto3.client('glue')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    file_path = f"s3://{bucket}/{key}"

    glue.start_job_run(
        JobName='fraud-cleaning-job',
        Arguments={
            '--input_path': file_path
        }
    )

    return {
        'statusCode': 200,
        'body': f'Glue Job Started for {file_path}'
    }