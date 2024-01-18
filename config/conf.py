import sys
import yaml
import logging
from utils.settings import settings

def load():
    logger = logging.getLogger('main')
    try:
        config = yaml.load(open(settings.configPath, 'r'), Loader=yaml.FullLoader)
    except:
        logger.error('Cant load config')
        sys.exit(1)

    if config:
        if 'events' in config:
           logger.info('Events loaded')
        else:
            logger.warn('Events not defined - loading defaults')
            config['events'] = {}
        return config
    else:
        logger.error('Unable to load config')
        sys.exit(1)