import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime as dt
import os


now = dt.now().strftime('%m/%d/%y %H:%M')
today = dt.now().strftime('%y%m%d')

df = pd.read_csv('data/candidate_totals.csv')

# Totals by party
sum_df = df.groupby(['party_full'])['individual_itemized_contributions'].sum()
sum_df_other = sum_df[~sum_df.index.isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY', 'INDEPENDENT'])]
sum_df = sum_df[sum_df.index.isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY', 'INDEPENDENT'])]
sum_df['OTHER'] = sum_df_other.sum()

fig, ax = plt.subplots(figsize=[16,7])
palette = ['blue', 'orange', 'red', 'green']
sb.barplot(y=sum_df.values, x=sum_df.index, hue=sum_df.index, orient='v', palette=palette, legend=False, ax=ax)
for container in ax.containers:
    ax.bar_label(container, fmt=lambda x: f'${x:,.0f}')
plt.suptitle('2026 Total Individual Itemized Contributions to Candidates by Party', fontsize=16)
ax.set_title('Last Updated ' + str(now), fontsize=12, fontstyle='italic')
ax.set_xlabel('Party', fontsize=12)
ax.set_ylabel('Total', fontsize=12)
ax.set_yticks([0, 100000000, 200000000, 300000000, 400000000, 500000000], labels=['$0', '$100M', '$200M', '$300M', '$400M', '$500M'])

try:
    os.rename('charts/individual_contributions.png', 'fec_charts/archive/individual_contributions_' + today + '.png')
except:
    pass

plt.savefig('charts/individual_contributions.png', bbox_inches='tight', dpi=150)