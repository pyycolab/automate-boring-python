# the requests module download webpage
import requests, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
logging.debug(type(res))
logging.debug(res.status_code == requests.codes.ok)
logging.debug(res.status_code)
logging.debug(requests.codes.ok)
# 200 is html for ok
logging.debug('The length of the text is ' + str(len(res.text)))
print(res.text[:9000])
