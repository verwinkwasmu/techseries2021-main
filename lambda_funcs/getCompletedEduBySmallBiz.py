import json
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('education_completed')


def lambda_handler(event, context):
    try:
        response = table.query(
        KeyConditionExpression=Key('smallBizID').eq(event['smallBizID'])
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
