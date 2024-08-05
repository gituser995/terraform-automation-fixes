import boto3
import json

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    gitlab_trigger_url = "https://gitlab.com/api/v4/projects/dd21b2dd07014f83eb2dd60f0c4cc79d341874d6/trigger/pipeline"
    gitlab_token = "glptt-35599ccfb272f0a01c1da6c9d3e4f2e7365620cb"
    
    # Trigger the GitLab pipeline
    response = sns_client.publish(
        TopicArn='arn:aws:sns:us-east-2:663485453166:securityhublambda',
        Message=json.dumps({'default': json.dumps(event)}),
        MessageStructure='json'
    )
    
    # Add code to trigger GitLab pipeline
    return {
        'statusCode': 200,
        'body': json.dumps('GitLab pipeline triggered')
    }

