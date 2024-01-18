import logging
from utils.settings import settings

def load():
  logger = logging.getLogger('main')
  log_level = logging.getLevelName(settings.logLevel)
  logger.setLevel(log_level)

  channeling = logging.StreamHandler()
  formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%m-%Y %I:%M:%S')

  channeling.setFormatter(formatter)
  logger.addHandler(channeling)

  return logger
