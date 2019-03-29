import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


times = []
data = pd.read_csv('data.csv', delimiter=',')
for i in range(0, len(data)):
    readable = time.ctime(data['review/time'][i])
    times.append(int(readable[-4:]))

data['year'] = times

sns.set()
colors = sns.color_palette("GnBu", 1)
data['year'].plot.hist(bins = 14, rwidth = 1, color = colors)
plt.xlabel('Year')
plt.title('Quantity of reviews in respective years')
plt.savefig('Time-score.png')



