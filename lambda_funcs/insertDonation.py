import json
import boto3
import uuid
from datetime import datetime

now = datetime.now()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('donation_transactions')

def lambda_handler(event, context):
    id = str(uuid.uuid4())
    response = table.put_item(
        Item = {
            'id': id,
            'userID': event['userID'],
            'smallBizID': event['smallBizID'],
            'amount': event['amount'],
            'timestamp': now.strftime("%d/%m/%Y %H:%M:%S")
        }
    )
    
    return {
        'statusCode': 200,
        'body': "Success!"
    }