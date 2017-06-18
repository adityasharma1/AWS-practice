import json
from datetime import datetime


def main():
    #cfn_client = b.client('cloudformation')
    cfn_template = datetime.now().strftime("%Y%m%d-%H%M%S") + '_cfn_template.json'

    data = {
        "AWSTemplateFormatVersion" : "version date",

        "Description" : "JSON string",

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