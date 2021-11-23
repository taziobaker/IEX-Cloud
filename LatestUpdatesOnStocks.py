import pandas as pd
import requests
from termcolor import colored as cl
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (15,8)

def get_latest_updates(*symbols):
    for i in symbols:
        ticker = i
        iex_api_key = 'pk_efb2ea03800647c1b4ac74094e77f29d'
        api_url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={iex_api_key}'
        df = requests.get(api_url).json()
        print(cl('Latest Updates of {}\n--------------'.format(ticker), attrs = ['bold']))
        attributes = ['symbol', 
                      'latestPrice', 
                      'marketCap', 
                      'peRatio']
        for i in attributes:
            print(cl('{} :'.format(i), attrs = ['bold']), '{}'.format(df[i]))    
        print(cl('--------------\n', attrs = ['bold']))

get_latest_updates('AMC', 'GME', 'SNDL', 'BB', 'CLOV')
