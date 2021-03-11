import boto3
from boto3.dynamodb.conditions import Key
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('attendance2')

def lambda_handler(event,context):
    grps = ["Ganguly","sehwag","kapildev"]  
    vals = []
    for i in grps:
        response = table.scan(FilterExpression=Key('name').eq(i))
        print(response)
        vals.append(len(response['Items']))
    return vals