import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime as dt
import os

now = dt.now().strftime('%m/%d/%y %H:%M')
today = dt.now().strftime('%y%m%d')

df = pd.read_csv('data/candidate_totals.csv')

sum_df = df.groupby(['party_full'])[['receipts', 'disbursements']].sum()
sum_df = sum_df[sum_df.index.isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY', 'INDEPENDENT'])]

df_other = df[~df['party_full'].isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY', 'INDEPENDENT'])]
df_other['party_full'] = 'OTHER'
sum_df_other = df_other.groupby('party_full')[['receipts', 'disbursements']].sum()

sum_df = pd.concat([sum_df, sum_df_other])

parties = sum_df.index
party_totals = {
    'Receipts': (sum_df['receipts'].values),
    'Disbursements': (sum_df['disbursements'].values)
}

fig, ax = plt.subplots(figsize=[15, 8], layout='constrained')

res = ax.grouped_bar(party_totals, tick_labels=parties, group_spacing=1)
for container in res.bar_containers:
    ax.bar_label(container, padding=3, fmt=lambda x: f'${x:,.0f}')

plt.suptitle('2026 Total Candidate Receipts and Dibursements', fontsize=16)
ax.set_title('Last Updated ' + str(now), fontsize=12, fontstyle='italic')
ax.set_xlabel('Party', fontsize=12)
ax.set_ylabel('Total', fontsize=12)
ax.set_yticks([0, 250000000, 500000000, 750000000, 1000000000, 1250000000], labels=['$0', '$250M', '$500M', '$750M', '$1B', '$1.25B'])
ax.legend()

try:
    os.rename('fec_charts/candidate_totals.png', 'fec_charts/archive/candidate_totals_' + today + '.png')
except:
    pass

plt.savefig('fec_charts/candidate_totals.png', bbox_inches='tight', dpi=150)