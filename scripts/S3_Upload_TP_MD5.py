import requests

# The invoke URL of the API Gateway
invoke_url = 'https://.execute-api.us-east-2.amazonaws.com/Dev/'

# The path parameters required by the API Gateway
bucket_name = 'ip-shun'
object_key = 'ipshun.txt.md5'

# The full URL to call the API Gateway
full_url = f"{invoke_url}/{bucket_name}/{object_key}"

# The local path to the file you want to upload
file_path = 'ipshun.txt.md5'

# Open the file in binary mode and send the PUT request
with open(file_path, 'rb') as file_data:
    response = requests.put(full_url, data=file_data)

# Check the response
if response.status_code == 200:
    print("File uploaded successfully.")
else:
    print(f"Failed to upload file. Status code: {response.status_code}")

