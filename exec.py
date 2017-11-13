import sys
import logging
try:
    a+b
except:
    exc = sys.exc_info()
    logging.error(exc[1]）
#    print exc
