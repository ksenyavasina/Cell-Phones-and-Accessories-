import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('data.csv', delimiter=',')

HelpfulnessNumerator = list()
HelpfulnessDenominator = list()
for i in data['review/helpfulness']:
    i = i.split('/')
    HelpfulnessNumerator.append(int(i[0]))
    HelpfulnessDenominator.append(int(i[1]))

data['HelpfulnessNumerator'] = HelpfulnessNumerator
data['HelpfulnessDenominator'] = HelpfulnessDenominator
data['Helpful%'] = np.where(data['HelpfulnessDenominator'] > 0, data['HelpfulnessNumerator'] / data['HelpfulnessDenominator'], -1)
data['HelpfulIntervals'] = pd.cut(data['Helpful%'], bins = [-1, 0, 0.2, 0.4, 0.6, 0.8, 1.0], labels = ['Empty', '0-20%', '20-40%', '40-60%', '60-80%', '80-100%'], include_lowest = True)

df = data.groupby(['review/score', 'HelpfulIntervals']).agg({'nr': 'count'})
df = df.unstack()
df.columns = df.columns.get_level_values(1)
fig = plt.figure(figsize=(10,7))


sns.heatmap(df[df.columns[::-1]].T, cmap = 'GnBu', linewidths=.5, annot = True, fmt = 'd', cbar_kws={'label': '#reviews'})
plt.yticks(rotation=0)
plt.title('Was this review helpful for other users')
plt.xlabel('Score')
plt.ylabel('Hepful Intervals')
plt.savefig('Helpfull-score.png')