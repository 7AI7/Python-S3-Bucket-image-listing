# Python Script to Upload Images to S3 with Metadata

## Description:

This Python script uploads images to an S3 bucket while adding image dimensions as metadata. It also provides functionality to list files in the bucket and upload a specific file based on user input.

## Prerequisites:

Python 3.x

boto3 library ('pip install boto3')

PIL/Pillow library ('pip install Pillow')

AWS credentials configured for boto3

## Usage:

Replace the placeholder values for aws_access_key_id, aws_secret_access_key, and YOUR_BUCKET_NAME with your actual AWS credentials and bucket name.

Ensure the image_path variable in the upload_image_with_metadata function points to the correct local directory containing images.

Run the script.

The script will list the files in the bucket.

Enter the desired file index to upload the corresponding image.
