import json
import boto3
import os
import sys
import uuid

def deleteFile(bucket, key):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket,key)
    obj.delete()
    return True

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    for record in event['Records']:
        key = record['s3']['object']['key']
        print("Find record at {}!".format(key))
        
        if key.split("/")[0] != 'uploadsEncrypted':
            bucket = record['s3']['bucket']['name']
            downloadPath = '/tmp/{}'.format(uuid.uuid4())
            s3.download_file(bucket,key,downloadPath)
            data=open(downloadPath,'rb')
            
            s3.put_object(Bucket=bucket, Key='uploadsEncrypted/'+key.split("/")[-1], ServerSideEncryption="AES256", Body=data)
            
            deleteFile(bucket,key)
            print("Noooooice")
        
    return {
        'statusCode': 200,
        'body': json.dumps("Welcome from Lambda! {}".format(key))
    }
