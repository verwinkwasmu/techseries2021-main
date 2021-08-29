import json
import boto3
import uuid
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('education_completed')

def lambda_handler(event, context):
    response = table.put_item(
        Item = {
            'smallBizID': event['smallBizID'],
            'eduID': event['eduID'],
        }
    )
    
    return {
        'statusCode': 200,
        'body': response
    }