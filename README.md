# Lambda-S3-Convert-CSV-JSON
Lambda function for AWS to convert CSV file in a S3 bucket to JSON

`````````````````````````````````````````````````````
targetbucket = '<BUCKET_NAME>'     # s3 bucket containing CSV file
csvkey = '<FILENAME>.csv'          # filename of the CSV file
jsonkey = '<FILENAME>.json'        # desired output name for JSON file

Trigger on S3 event:
Bucket: <BUCKET_NAME>
Event type: ObjectCreated
Prefix: <FILENAME>
Suffix: csv
