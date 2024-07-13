import os
from PIL import Image
import boto3 

# Configure S3 access (replace with your credentials)
s3_client = boto3.client('s3',
                        aws_access_key_id='your access id',
                        aws_secret_access_key='your access key')
bucket_name = 'YOUR bucket name'  

def get_image_size(image_path):
    """
    Opens an image and returns its height and width.
    """
    try:
        with Image.open(image_path) as image:
            width, height = image.size
            return width, height
    except Exception as e:
        print(f"Error opening image: {image_path} ({e})")
        return None, None

def upload_image_with_metadata(image_path,files):
    #Uploads an image to S3 bucket and adds height and width as metadata.
    
    filename = os.path.basename(image_path)
    try:
        width, height = get_image_size(image_path)
        if width and height:
            metadata = {'width': str(width), 'height': str(height)}
            filesname= files + filename   #specifying file directory path to upload image
            s3_client.upload_file(image_path, bucket_name, filesname, ExtraArgs={'Metadata': metadata})
            print(f"Uploaded {filename} with size: {width}x{height}")
        else:
            print(f"Failed to get size for {filename}")
    except Exception as e:
        print(f"Error uploading {filename}: {e}")


#accessing a file from directory in bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket("polaroidfiles")
filenamesinBucket = []

for filename in os.listdir('./'):
    # Check if it's an image file
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join('./', filename)
        #upload_image_with_metadata(image_path, files)[]
for obj in bucket.objects.all():
    names = obj.key  # obj.key represents the file name
    filenamesinBucket.append(names)
[print (f"{n}.{ITEM}") for n , ITEM in enumerate(filenamesinBucket)]

# input to access the particular file in bucket
x = int(input("Enter the number to upload in:"))
try:
    for n in len (filenamesinBucket):
        if n == x:
            files = filenamesinBucket[n]
            break
        else:
            continue
except:
    print ("Enter valid number!!")
upload_image_with_metadata(image_path,files)