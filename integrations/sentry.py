import requests
import logging
from utils.settings import settings
import sentry_sdk

def alert(event,config,thisHost,timestamp):
    logger = logging.getLogger('main')

    ## Define payload
    payload = {
      "host": thisHost,
      "event": event['Action'],
      "type": event['Type'],
      "time": timestamp,
      "id": event['Actor']['ID']
    }

    if 'name' in event['Actor']['Attributes']:
      payload['name'] = event['Actor']['Attributes']['name']

    if settings.sentry_env:
        sentry_sdk.set_tag('environment', settings.sentry_env)
    else:
        sentry_sdk.set_tag('environment', 'dev')

    try:
        for key in payload:
            sentry_sdk.set_tag(key, payload[key])
        sentry_sdk.capture_exception(Exception(payload))

    except Exception as e:
        logger.error('{}: {}'.format(__name__,e))
        sentry_sdk.capture_exception(e)

