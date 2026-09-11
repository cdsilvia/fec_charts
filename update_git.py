import subprocess
import os

os.chdir('charts')

subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', 'Update charts'])
subprocess.run(['git', 'push'])


# def push_update(file, commit_description):
#     subprocess.run(['git', 'add', file])
#     subprocess.run(['git', 'commit', '-m', commit_description])
#     subprocess.run(['git', 'push'])

# push_update('README.md', 'Update README')
# push_update('individual_contributions.png', 'Update individual contributions')
# push_update('committee_contributions.png', 'Update committee contributions')
# push_update('candidate_totals.png', 'Update candidate totals')