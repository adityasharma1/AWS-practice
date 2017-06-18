import boto3 as b
import logging_module

def create_bucket (bucket_name,s3_client,bucket_region):

    ec2_client = b.client('ec2',region_name='us-west-2')
    logging_module.logger.info("this is the s3 client{0} and name = {1}".format(s3_client, bucket_name))

    #check if bucket name is unique
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    correct_region_name = False
    for region in regions:
        if (region == bucket_region):
            correct_region_name = True
    #bucket_to_create = s3_client.Bucket(bucket_name)
    #print(bucket_to_create)

    #if bucket_to_create is None:
    bucket_to_create = s3_client.create_bucket(Bucket=bucket_name)
    #bucket_list = s3_client.buckets.all()
    #print(bucket_list)
    #for bucket in bucket_list:
    #    if (bucket_to_create == bucket):
     #       print (bucket_to_create)
    bucket_arn = ""
    return bucket_arn


def main():
    s3client = b.client('s3')
    bucket_region = "us_west_1"
    create_bucket("aditya_sharma_bucket123", s3client, bucket_region)


if __name__ == '__main__':main()