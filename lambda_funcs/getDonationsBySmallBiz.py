import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    smallBizID = event["smallBizID"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('donation_transactions')
    
    try:
        response = table.scan(
            FilterExpression=Attr('smallBizID').eq(smallBizID)
        )
        
    except ClientError as e:
        print(e.response['Error']['Message'])    
    
    return response