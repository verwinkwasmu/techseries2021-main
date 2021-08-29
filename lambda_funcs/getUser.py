import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    userID = event["userID"]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Users')
    
    try:
        response = table.query(
            KeyConditionExpression=Key('userID').eq(userID)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response

