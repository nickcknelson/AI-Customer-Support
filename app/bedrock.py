import boto3
import json

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

prompt = "what is the full-form of RAG in case of large language models?"


kwargs = {
  "modelId": "anthropic.claude-3-5-sonnet-20240620-v1:0",
  "contentType": "application/json",
  "accept": "application/json",
  "body": json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": [
      {
        "role": "user",
        "content": [
         
          {
            "type": "text",
            "text": prompt
          }
        ]
      }
    ]
  })
}


response = bedrock_runtime.invoke_model(**kwargs)

body = json.loads(response['body'].read())

print(body)