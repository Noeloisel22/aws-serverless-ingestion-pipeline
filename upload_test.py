import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

# Configuration variables
target_bucket = "nloisel-2026-data-pipeline" 
local_file_path = "test_data.txt"
s3_object_key = "raw_data/test_data.txt"  


try:
    print(f"Initiating upload of '{local_file_path}' to S3...")
    print(f"Destination: s3://{target_bucket}/{s3_object_key}")
    
    s3_client.upload_file(local_file_path, target_bucket, s3_object_key)
    
    print("Success: File successfully uploaded to AWS S3.")
except Exception as e:
    print(f"AWS Upload Error: {e}")