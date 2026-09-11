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
authorized_committees = df.groupby(['party_full'])['transfers_from_other_authorized_committee'].sum()
authorized_committees = authorized_committees[authorized_committees.index.isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY'])]

other_committees = df.groupby(['party_full'])['other_political_committee_contributions'].sum()
other_committees = other_committees[other_committees.index.isin(['DEMOCRATIC PARTY', 'REPUBLICAN PARTY'])]

fig, ax = plt.subplots(figsize=[16,7])
parties = other_committees.index
contributions = {
    'Authorized Committees': authorized_committees.values,
    'Other Political Committees': other_committees.values
}
width = 0.6

bottom = np.zeros(2)

for type, contribution in contributions.items():
    p = ax.bar(parties, contribution, width, label=type, bottom=bottom)
    bottom += contribution
    ax.bar_label(p, label_type='center', fmt=lambda x: f'${x:,.0f}')

plt.suptitle('2026 Committee Contributions to Candidates by Party', fontsize=16)
ax.set_title('Last Updated ' + str(now), fontsize=12, fontstyle='italic')
ax.set_xlabel('Party', fontsize=12)
ax.set_ylabel('Total', fontsize=12)
ax.legend()
ax.set_yticks([0, 100000000, 200000000, 300000000], labels=['$0', '$100M', '$200M', '$300M'])

try:
    os.rename('fec_charts/committee_contributions.png', 'fec_charts/archive/committee_contributions_' + today + '.png')
except:
    pass

plt.savefig('fec_charts/committee_contributions.png', bbox_inches='tight', dpi=150)