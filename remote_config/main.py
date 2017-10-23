import json
from functools import lru_cache

import boto3

client = boto3.client('lambda')


@lru_cache(maxsize=32)
def get_config_key(key):
    response = client.invoke(
        FunctionName='remote-config',
        InvocationType='RequestResponse',
        Payload=json.dumps({'key': key}),
    )

    return json.loads(response['Payload'].read().decode('utf-8'))
