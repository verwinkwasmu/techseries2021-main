import json
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('education_info')


def lambda_handler(event, context):
    try:
        response = table.get_item(Key={'eduID': event['eduID']})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
