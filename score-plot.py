import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data.csv', delimiter=',')
df = data.groupby(['product/productId']).mean().sort_values(by=['review/score'],  ascending=False)


labels = '5', '4', '3', '2', '1'
sizes = [len((df[df['review/score'] == 5.0])), len((df[df['review/score'] == 4.0])), len((df[df['review/score'] == 3.0])), len((df[df['review/score'] == 2.0])), len((df[df['review/score'] == 1.0]))]

colors = sns.color_palette("GnBu", 5)
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title('Score of reviews')
plt.savefig('Score of reviews.png')

