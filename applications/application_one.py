import logging
from project_one import ProjectOne
import sys

# turn on logging
logger = logging.getLogger()
logger.setLevel( logging.DEBUG)

# main
def main():
    # setup handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    logger.info('===================================>> pyspark project')
    project = ProjectOne()
    project.run()

    logger.info('END')

if __name__ == '__main__':
    main()