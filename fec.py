## API Limits: 1,000 calls per hour, 100 results per page
import pandas as pd 
import requests
import matplotlib 
import json
import base64
from datetime import datetime as dt
import os

now = dt.now().strftime('%m/%d/%y %H:%M')
today = dt.now().strftime('%y%m%d')

# Stored API key
file = open('api_key.txt')
content = file.read()
file.close()
api_key = base64.b64decode(content)

base_url = 'https://api.open.fec.gov'
headers = {'X-Api-Key': api_key}

def fec_api_pull(end_url, base_parameters, dedupe_columns, csv_name):
    print('Pulling from ' + base_url + end_url)
    data = requests.get(base_url + end_url, headers=headers, params=base_parameters)
    data_json = json.loads(data.text)
    current_page = data_json['pagination']['page']
    total_pages = data_json['pagination']['pages']
    print('Page ' + str(current_page) + ' of ' + str(total_pages), end='\r')

    df = pd.DataFrame(data=data_json['results'])
    current_page += 1

    while current_page <= total_pages:
        these_parameters = base_parameters.copy()
        these_parameters.update({'page': current_page})
        this_data = requests.get(base_url + end_url, headers=headers, params=these_parameters)
        this_json = json.loads(this_data.text)
        this_df = pd.DataFrame(data=this_json['results'])
        df = pd.concat([df, this_df], ignore_index=True)
        if current_page < total_pages:
            print('Page ' + str(current_page) + ' of ' + str(total_pages), end='\r')
        else:
            print('Page ' + str(current_page) + ' of ' + str(total_pages))

        current_page += 1

    df.drop_duplicates(subset=dedupe_columns, inplace=True)
    try:
        os.rename('data/' + csv_name + '.csv', 'data/archive/' + csv_name + '_' + today + '.csv')
    except:
        pass
    
    df.to_csv('data/' + csv_name + '.csv', index=False)
    print('Success.')