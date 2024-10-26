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

    logger.info('===================================>> pyspark project START')
    logger.info('===================================>> pyspark project START')
    logger.info('===================================>> pyspark project START')
    logger.info('===================================>> pyspark project START')
    logger.info('===================================>> pyspark project START')
    project = ProjectOne()
    project.run()

    logger.info('===================================>> pyspark project END')
    logger.info('===================================>> pyspark project END')
    logger.info('===================================>> pyspark project END')
    logger.info('===================================>> pyspark project END')
    logger.info('===================================>> pyspark project END')

if __name__ == '__main__':
    main()