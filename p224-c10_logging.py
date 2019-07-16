import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# to export log message to files
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# simple factorial script
def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
        logging.debug('End of factorial(%s)' % (n))
    return total

factorial(10)

# logging levels
logging.debug('Some debugging details.')
logging.info('The loggin module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# disable logging
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
