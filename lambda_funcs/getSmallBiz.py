import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # TODO implement
    smallbizID = event["smallbizID"]
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('SmallBusinesses')
    
    try:
        response = table.scan(
            FilterExpression=Attr('smallbizID').eq(smallbizID)
        )
        
    except ClientError as e:
        print(e.response['Error']['Message'])    
    
    return response
