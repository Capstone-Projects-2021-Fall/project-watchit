import presigned as pr
import pymongo_video as pv
import boto3
import os
from datetime import datetime

def upload_video(count):
    """
    This function is called after video is finished recording. 

    :param count: used in naming of the video, used in a strictly iterative fashion. 
    """

    name = f"output{count}.avi"

    s3_client = boto3.client(
                        's3',
                        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                        aws_secret_access_key=os.environ.get('AWS_SECRET_KEY')
                        )
                        
    dbname = pv.get_database()
    collection_name = dbname["Test_Videos"]

    url = pr.generate_presigned_url(s3_client, "put_object", {"Bucket": os.environ.get('AWS_BUCKET_NAME'), "Key": name}, 30)

    pr.upload_video(url, name)
    pv.new_video(collection_name, "seconduser@user.com", {"videoID" : count, "url" : f"https://{os.environ.get('AWS_BUCKET_NAME')}.s3.amazonaws.com/{name}", "name": name, "time": datetime.now()})