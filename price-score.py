import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data.csv', delimiter=',')
price = list()
for i in data['product/price']:
    if i == ' unknown':
        price.append('unknown')
    elif float(i) <= 10:
        price.append('0-10')
    elif float(i) > 10 and float(i) <= 25:
        price.append('11-25')
    elif float(i) > 25 and float(i) <= 50:
        price.append('26-50')
    elif float(i) > 50 and float(i) <= 100:
        price.append('51-100')
    elif float(i) > 100 and float(i) <= 200:
        price.append('101-200')
    elif float(i) > 200 and float(i) <= 300:
        price.append('201-300')
    elif float(i) > 300 and float(i) <= 400:
        price.append('301-400')
    elif float(i) > 400 and float(i) <= 500:
        price.append('401-500')
    elif float(i) > 500:
        price.append('>500')

data['PriceIntervals'] = price


df = data.groupby(['review/score', 'PriceIntervals']).agg({'nr': 'count'})
df = df.unstack()
new_order = [0, 2, 4, 7, 1, 3, 5, 6, 8, 9]
df = df[df.columns[new_order]]
df.columns = df.columns.get_level_values(1)
fig = plt.figure(figsize=(10,7))

sns.heatmap(df[df.columns[::-1]].T, cmap = 'GnBu', linewidths=.5, fmt = '.0f',  annot = True, cbar_kws={'label': '#reviews'})
plt.yticks(rotation=0)
plt.title('Relationship between price and score of product')
plt.xlabel('Score')
plt.savefig('Price-score.png')


data_rec = data.groupby(['product/title', 'PriceIntervals']).agg({'review/score':['count', 'mean']})
data_rec.columns = data_rec.columns.get_level_values(1)
data_rec.columns = ['Score count', 'Score mean']
data_user = data_rec[data_rec['Score count'] > 30]
data_user = data_user.sort_values(by = 'Score mean', ascending = False)
print(data_user.head(10))