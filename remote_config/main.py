import json
from functools import lru_cache

import boto3

client = boto3.client('lambda')


@lru_cache(maxsize=32)
def get_config_key(key, env="PRD"):
    response = client.invoke(
        FunctionName='remote-config',
        InvocationType='RequestResponse',
        Payload=json.dumps({'key': key, 'env': env}),
    )

    return json.loads(response['Payload'].read().decode('utf-8')).get('value')
