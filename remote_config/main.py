import json
from functools import lru_cache

import boto3
import sys, os

client = boto3.client('lambda')

DEV = "DEV"
PRD = "PRD"
STG = "STG"
LOCAL = "LOCAL"


def get_env():
    for env in sys.argv:
        if DEV == env.upper():
            return DEV
        if PRD == env.upper():
            return PRD
        if STG == env.upper():
            return STG
        if LOCAL == env.upper():
            return LOCAL

    if os.environ['APP_ENV'].upper() in [DEV, PRD, STG, LOCAL]:
        return os.environ['APP_ENV'].upper()

    return PRD


@lru_cache(maxsize=32)
def get_config_key(key):

    env = get_env()

    response = client.invoke(
        FunctionName='remote-config',
        InvocationType='RequestResponse',
        Payload=json.dumps({'key': key, 'env': env}),
    )

    return json.loads(response['Payload'].read().decode('utf-8')).get('value')
