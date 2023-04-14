import json
from redis import RedisCluster

from config import redis_host, redis_port

r = RedisCluster(host=redis_host, port=redis_port)
print("Connected to Redis")

def get_data(token):
    print(f"Get data:\ntoken {token}")
    try:
        data = r.get(token)
    except:
        return 500
    if data is None:
        return 404
    return data

def lambda_handler(event, context):
    try:
        # REST invocation
        body = json.loads(event.get('body'))
    except:
        # Direct Lambda invocation
        body = event
    action = body.get("action")
    if action is None:
        return {
            'status': 'error',
            'code': 400,
            'message': f"No action to perform"
        }
    token = body.get("token")
    if not isinstance(token, str):
        return {
            'status': 'error',
            'code': 400,
            'message': f"Token {token} isn't a string"
        }
    if action == "get":
        serial_number = get_data(token)
        if serial_number == 500:
            return {
                'status': 'error',
                'code': 500,
                'message': "DB connection error"
            }
        elif serial_number == 404:
            return {
                'status': 'error',
                'code': 404,
                'message': f"Data not found by token {token}"
            }
        else:
            return {
                'status': 'success',
                'code': 200,
                'payload': {
                    "data": {
                        "primaryFields": [
                            {
                                "changeMessage": "New card %@",
                                "key": "serialnumber",
                                "label": "Serial number",
                                "value": serial_number,
                            },
                        ],
                    },
                },
                'serial_number': serial_number
            }
    else:
        return {
            'status': 'error',
            'code': 400,
            'message': f"Unrecognized action {action}"
        }
