import redis
import json
import os
from datetime import datetime

def get_redis_connection():
    host = os.getenv('LDM_REDIS_HOST', 'localhost')
    port = int(os.getenv('LDM_REDIS_PORT', 6379))
    db = int(os.getenv('LDM_REDIS_DB', 0))
    return redis.Redis(host=host, port=port, db=db, decode_responses=True)

def fetch_engagements():
    r = get_redis_connection()
    engagements = r.lrange('engagements', 0, -1)
    result = []
    for entry in engagements:
        data = json.loads(entry)
        # Ensure tuple order matches: status, client_engagement, date, major_urgent_callouts, slack_link
        # Convert date to string for compatibility
        result.append((
            data.get('status'),
            data.get('client_engagement'),
            data.get('date'),
            data.get('major_urgent_callouts'),
            data.get('slack_link')
        ))
    return result

