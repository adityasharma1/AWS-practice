import boto3 as b
import logging_module

def create_bucket (bucket_name,s3_client,bucket_region):

    s3client = b.client('s3')
    logging_module.logger.info("this is the s3 client{0} and name = {1}".format(s3_client, bucket_name))

    #check if bucket name is unique
    print(s3_client.list_buckets())
    bucket_arn = ""
    return bucket_arn


def main():
    s3client = b.client('s3')
    bucket_region = "us_west_1"
    create_bucket("name", s3client, bucket_region)


if __name__ == '__main__':main()