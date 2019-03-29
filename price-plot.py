import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv', delimiter=',')



df = data.drop_duplicates('product/productId', inplace=False)
df1 = df[df['product/price'] != ' unknown']

sns.set()
colors = sns.color_palette("GnBu", 1)
b = [0,25,50,75,100,200,300,400,500]
df1['product/price'].astype('float64').plot.hist(bins = b, rwidth = 1, color = colors)
plt.xlabel('Price')
plt.title('Price of products')
plt.savefig('Price of products.png')