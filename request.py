import requests
from PIL import image
from StringIO import StringIO
query = 'hat'
url = 'https://newyork.craigslist.org/search/sss?query={}&sort=rel'.format(query)

