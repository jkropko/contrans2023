import numpy as np
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import os

root = 'https://maps.spirithalloween.com'
endpoint = '/api/getAsyncLocations'
parameters = {'template':'domain',
              'level':'domain',
              'lat': 40.380028, 
              'lng': -97.910156,
              'radius': 1800,
              'limit': 2000}
r = requests.get(root + endpoint,
                params = parameters)

myjson = json.loads(r.text)
mysoup = BeautifulSoup(myjson['markers'][3]['info'], 'html.parser')
mylist = [BeautifulSoup(x['info'], 'html.parser').find_all('div', 'address-two')[0].text for x in json.loads(r.text)['markers']]
mylist = [x for x in mylist if 'Former' in x]

pd.set_option('display.max_rows', 440)
pd.Series(mylist).value_counts()
