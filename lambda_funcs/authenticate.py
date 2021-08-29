import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Account')

def lambda_handler(event, context):
  email = event["email"]
  password = event["password"]
  
  try:
    response = table.query(
        KeyConditionExpression=Key('email').eq(email)
    )
    items = response['Items']
    if password == items[0]['password']:
        return response
    else:
        return "Error user is not authenticated"
  except ClientError as e:
      print(e.response['Error']['Message'])
  else:
      return response