import boto3
import botocore

def s3_download(s3url, destination_directory):

    path_str = s3url.replace("s3://",'')
    BUCKET_NAME = path_str.split('/')[0]
    KEY = '/'.join(path_str.split('/')[1:])
    fn = path_str.split('/')[-1]
    full_fn = f'{destination_directory}/{fn}'

    #print(f'bucket = {BUCKET_NAME}, key = {KEY}, fn={fn}, full={full_fn}')
    print('.', fn)
    
    # BUCKET_NAME = 'my-bucket' # replace with your bucket name
    # KEY = 'my_image_in_s3.jpg' # replace with your object key
    
    s3 = boto3.resource('s3')
    
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, full_fn, {'RequestPayer':'requester'})
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
