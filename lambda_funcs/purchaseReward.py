import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('purchasedRewards')

def lambda_handler(event, context):
  id = str(uuid.uuid4())
  voucherID = event['voucherID']
  voucherName = event['voucherName']
  userID = event['userID']
  costPrice = event['costPrice']
  
  try:
    response = table.put_item(
      Item={
        'purchaseID': id,
        'voucherID': voucherID,
        'voucherName': voucherName,
        'userID': userID,
        'costPrice': costPrice
      })
      
  except ClientError as e:
      print(e.response['Error']['Message'])
  else:
      return response