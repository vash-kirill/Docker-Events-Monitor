import time
from utils.settings import settings
from utils import log, streamer
from config import conf
from integrations import sentry
import signal
import sys
import sentry_sdk

logger = log.load()
config = conf.load()

def sendAlert(event,timestamp,selfhost):
  if settings.sentry_dsn:
    logger.info('Alert triggered: {}, {}, {}'.format(event['Type'],event['Action'],event['Actor']['ID']))
    sentry.alert(event,config,selfhost,timestamp)

def main():
  # Initialize Docker events stream
  stream = streamer.stream()

  for event in stream[0]:
    logger.debug('Event: {}'.format(event))

    eventType = event['Type']
    eventAction = event['Action']
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(event['time']))

    if eventType in config['events']:
      if eventAction in config['events'][eventType]:
        sendAlert(event,timestamp,stream[1])

def shutdown(_signo, _stack_frame):
  logger.info('Recieved {}, shutting down'.format(_signo))
  sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, shutdown)
  signal.signal(signal.SIGTERM, shutdown)

  sentry_sdk.init(
    dsn=settings.sentry_dsn,
    environment=settings.sentry_env,
  )

  main()
