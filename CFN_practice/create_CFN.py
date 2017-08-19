import json
from datetime import datetime
import boto3 as b

def main():
    cfn_client = b.client('cloudformation',region_name='us-west-2')
    cfn_template = datetime.now().strftime("%Y%m%d-%H%M%S") + '_cfn_template.json'

    data = {
        "AWSTemplateFormatVersion" : datetime.now().strftime("%Y%m%d-%H%M%S"),

        "Description" : "test CFN",

        "Metadata" : {
            "template metadata": ""
        },

        "Parameters" : {
            "set of parameters": ""
        },

        "Mappings" : {
            "set of mappings": ""
        },

        "Conditions" : {
            "set of conditions": ""
        },

        "Transform" : {
            "set of transforms": ""
        },

        "Resources" : {
            "set of resources": ""
        },

        "Outputs" : {
            "set of outputs": ""
        }
    }
    with open(cfn_template, 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':main()