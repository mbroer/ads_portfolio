import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

df = pd.read_csv("C:/Users/Michael/Downloads/recipes.csv")

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

desc = [];
i = 0;

for url in df['url']:
  i+=1

  if i<7991:
    continue;

  req = requests.get(url, headers)
  soup = BeautifulSoup(req.content, 'html.parser')
  d = soup.select("p[class^=typography_root_]")[0].getText();
  if not d:
    d = 'nan';

  print(i, d);
  desc.append(d)

arr = np.array(desc)

DF = pd.DataFrame(arr)
DF.to_csv("data1.csv")