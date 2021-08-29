import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    userID = event["userID"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('purchasedRewards')
    
    try:
        response = table.scan(
            FilterExpression=Attr('userID').eq(userID)
        )
        
    except ClientError as e:
        print(e.response['Error']['Message'])    
    
    return response
