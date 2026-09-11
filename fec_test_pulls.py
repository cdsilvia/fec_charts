## API Limits: 1,000 calls per hour, 100 results per page
import pandas as pd 
import requests
import matplotlib 
import json
import base64

api_key = base64.b64decode(b'ZFhJWEhsamY2dlNOd2ZiSlY2emZlSkxlM0R0U0JYRlNacGE5R1ZCVA==')

base_url = 'https://api.open.fec.gov'
headers = {'X-Api-Key': api_key}


# Pulling committees
parameters = {
    'per_page': 100,
    'cycle': 2026
}
data = requests.get(base_url + '/v1/totals/by_entity/', headers=headers, params=parameters)
data
data_json = json.loads(data.text)
df = pd.DataFrame(data=data_json['results'])
df.to_csv('totals_by_entity.csv', index=False)


# PAC and party entity totals
# ~10k records
parameters = {
    'per_page': 100,
    'cycle': 2026
}
data = requests.get(base_url + '/v1/totals/pac-party/', headers=headers, params=parameters)
print(data)
data_json = json.loads(data.text)
print(data_json['pagination'])
df = pd.DataFrame(data=data_json['results'])
df.to_csv('entity_totals_pac-party.csv', index=False)

# House and Senate
# 4,238
data = requests.get(base_url + '/v1/totals/house-senate/', headers=headers, params=parameters)
print(data)
data_json = json.loads(data.text)
print(data_json['pagination'])
df = pd.DataFrame(data=data_json['results'])
df.to_csv('entity_totals_house-senate.csv', index=False)

# IE-only
# 47
data = requests.get(base_url + '/v1/totals/ie-only/', headers=headers, params=parameters)
print(data)
data_json = json.loads(data.text)
print(data_json['pagination'])
df = pd.DataFrame(data=data_json['results'])
df.to_csv('entity_totals_ie-only.csv', index=False)



# grouping and formatting
net_contributions = df.groupby('party_full')['net_contributions'].sum()
net_contributions.apply(lambda x: f'${x:,.0f}')