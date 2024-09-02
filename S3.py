import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client("s3", region_name = 'ap-south-1')

def create_bucket(bucket_name):
    try:
        response = s3_client.create_bucket(Bucket = bucket_name,
                                           CreateBucketConfiguration={
                                               'LocationConstraint':'ap-south-1'
                                           })
        return response
    except ClientError as e:
        print("error is", e)

def list_buckets():
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket["Name"])
    return response

def upload_file(file_path, bucket_name, object_name = None):
    if object_name is None:
        object_name =  file_path

    try:
        response = s3_client.upload_file(file_path, bucket_name, object_name)

    except ClientError as e:
        print("error is", e)

def download_file(bucket_name, object_name, file_path): 
    response = s3_client.download_file(bucket_name, object_name, file_path)

def delete_object(bucket_name, object_name):
    response =s3_client.delete_object(Bucket = bucket_name, Key = object_name)

def delete_bucket(bucket_name):
    response = s3_client.delete_bucket(
        Bucket = bucket_name
    )
    return response

def main():
    create_bucket("demo-bucket-example-apexon")
    print(list_buckets())
    upload_file("C:/Users/kashy/OneDrive/Documents/Bridgelabz/exported2_data.csv", 'demo-bucket-example-apexon', 'exported_data.csv')
    download_file("demo-bucket-example-apexon", "exported_data.csv", "./aws_exported_data")
    delete_object("demo-bucket-example-apexon", "exported_data.csv")
    delete_bucket("demo-bucket-example-apexon")

if __name__ == '__main__':
    main()


