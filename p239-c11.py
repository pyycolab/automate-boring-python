import requests, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
# pass wb to write binary files
for chunk in res.iter_content(100000):
    # looping chop off the file into segment, make sure the module doesn't eat up too much memory
    playFile.write(chunk)
    logging.debug('Current file size is: ' + str(playFile.write(chunk)))

playFile.close()
