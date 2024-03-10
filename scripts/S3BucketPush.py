import boto3
import requests
import os

def upload_file_to_s3(file_path, bucket_name, key_name, authorization_token):
    # Create a presigned URL for S3 upload
    s3_client = boto3.client('s3')
    presigned_url = s3_client.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': bucket_name,
            'Key': key_name
        }
    )

    # Upload the file using requests library
    with open(file_path, 'rb') as file:
        files = {'file': (os.path.basename(file_path), file)}
        headers = {
            'Authorization': authorization_token
        }
        response = requests.put(presigned_url, files=files, headers=headers)

        # Check if the upload was successful
        if response.status_code == 200:
            print("File uploaded successfully")
        else:
            print("Failed to upload file")

# Example usage
file_path = '/path/to/your/file.txt'
bucket_name = 'your-bucket-name'
key_name = 'file.txt'
authorization_token = 'your-authorization-token'

upload_file_to_s3(file_path, bucket_name, key_name, authorization_token)

