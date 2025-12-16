import boto3
import json

def lambda_handler(event, context):
    try:
        # Get query parameters safely
        qsp = event.get('queryStringParameters')

        if not qsp or 'bucket' not in qsp or 'key' not in qsp:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Missing "bucket" or "key" query parameter.'})
            }

        bucket = qsp['bucket']
        key = qsp['key']

        # Generate presigned URL
        s3 = boto3.client('s3')
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': key},
            ExpiresIn=3600  # 1 hour expiry
        )

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'url': url})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
