import pandas as pd
import numpy as np

all_records = []
single_record = dict()
file = open('Cell_Phones_&_Accessories.txt', 'r')

lines = file.readlines()
i = 0
for line in lines:
    line = line.split(':')
    if line[0] != '\n':
        single_record[line[0]] = line[1].replace('\n', '')
        if line[0] == 'review/text':
            all_records.append(single_record)
            single_record = dict()


columnnames = ['product/productId', 'product/title', 'product/price', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score', 'review/time', 'review/summary', 'review/text']
data = pd.DataFrame(all_records, columns=columnnames)

number = range(1, len(all_records)+1)
data['nr'] = number

pd.DataFrame.to_csv(data, 'data.csv')

