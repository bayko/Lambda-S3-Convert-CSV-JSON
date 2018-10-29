import csv
import json
import boto3

def lambda_handler(event, context):
    
    targetbucket = 'BUCKET NAME'
    csvkey = 'FILENAME.csv'
    jsonkey = 'FILENAME.json'
    
    s3 = boto3.resource('s3')
    csv_object = s3.Object(targetbucket, csvkey)
    csv_content = csv_object.get()['Body'].read().splitlines()
    s3_client = boto3.client('s3')
    l = []
    
    for line in csv_content:
        x = json.dumps(line.decode('utf-8')).split(',')
        Username = str(x[0])
        Company = str(x[1])
        Title = str(x[2])
        y = '{ "Username": ' + Username + '"' + ','  \
            + ' "Company": ' + '"' + Company + '"' + ',' \
            + ' "Title": ' + '"' +  Title + '"' + '}'
        l.append(y)

    s3_client.put_object(
    	Bucket=targetbucket,
    	Body= str(l).replace("'",""),
    	Key=jsonkey,
    	ServerSideEncryption='AES256'
    )
