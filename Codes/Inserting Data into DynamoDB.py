import boto3
from datetime import datetime

dynamo = boto3.resource('dynamodb')
table = dynamo.Table("attendance2")
def lambda_handler(event, context):
    print(datetime.now())
    print("event")
    event={"timestamp":str(datetime.now()),"name":event['name'],"period":event["period"]}
    
    table.put_item(Item=event)
    return {"code":200,"message":"Successful insertion"}
