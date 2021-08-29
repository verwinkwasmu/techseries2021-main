import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    userID = event["userID"]
    amount = event["amount"]
    addOrMinus = event["addOrMinus"]
    
    
    if addOrMinus == "add":
        try:
            response = table.update_item(
                Key={
                    'userID': userID
                },
                ExpressionAttributeNames = {
                    '#coins': 'coins'
                },
                UpdateExpression="set #coins = coins + :val",
                ExpressionAttributeValues={
                    ':val': Decimal(amount)
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response    
            
    elif addOrMinus == "minus":
        try:
            response = table.update_item(
                Key={
                    'userID': userID
                },
                ExpressionAttributeNames = {
                    '#coins': 'coins'
                },
                UpdateExpression="set #coins = coins - :val",
                ExpressionAttributeValues={
                    ':val': Decimal(amount)
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response  
            
            
