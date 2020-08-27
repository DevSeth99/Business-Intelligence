# -*- coding: utf-8 -*-
"""
Created on Sun May 31 02:46:16 2020

@author: VIDHI
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#%%
#importing dataset1
xls = pd.ExcelFile(r'C:\Users\VIDHI\Desktop\fictionn.xlsx')
df1 = pd.read_excel(xls, 'S1')
#%%
df1.info()
df1.head()
df1.describe()

#%%
job = df1['Job Title']
print(job)

#%%
#frequency of type of job
jobcount = job.value_counts().plot(kind='bar', figsize = (14,8))
plt.xlabel('Job Title')
plt.ylabel('Total number of employees')
plt.title('Employees per job title')

#%%
plt.bar(job, df1['Total Pay'],)
plt.xlim(['Line Operator', 'VP of Sales'])
plt.show()

#%%
#grouping according to job title 
avg = df1.groupby('Job Title').mean()
#%%
#average pay according to profession
plt.bar(avg.index, avg['Total Pay'])
plt.xticks(rotation = 90)
plt.xlabel('job Title')
plt.ylabel('Average pay')
plt.title('Average pay for each profession')

#%%
#bonus for every position
plt.bar(df1['Job Title'], df1['Year End Bonus'])
plt.xticks(rotation = 90)
plt.xlabel('job Title')
plt.ylabel('Bonus payments')
plt.title('Year end bonuses for each profession')

#%%
#average bonus accoridng to profession
plt.bar(avg.index, avg['Year End Bonus'])
plt.xticks(rotation = 90)
#%%
#grouping based on savings plan
sv = df1.groupby('Savings Plan').mean()
print(sv)

#%%
#level of average savings in every plan
plt.bar(sv.index, sv['Savings'], color='red')
plt.xlabel('Savings Plan')
plt.ylabel('Average Savings')
plt.title('Average savings per saving plan')

#%%
#level of average pay per savings plan
plt.bar(sv.index, sv['Total Pay'])



#%%
#importing dataset2
df2 = pd.read_excel(xls, 'Finished Goods On-Hand')

#%%
#frequency of on hold
onhold = df2['On-hold'].value_counts()
x = onhold.plot(kind='pie')


#%%
#on hold analysis
yyx = sns.countplot(x='Description', hue = 'On-hold', data = df2)
yyx.set_xticklabels(yyx.get_xticklabels(), rotation=90)

#%%
#total quantity per item
plt.bar(df2['Description'], df2['Quantity'])
plt.xticks(rotation = 90)

#%%
#grouping based on average
averq = df2.groupby('Description').mean()
print(averq)

#%%
#average quantity per item
plt.bar(averq.index, averq['Quantity'])
plt.xticks(rotation = 90)

#%%
#importing data3
df3 = pd.read_excel(xls, 'Inventory Count')

#%%
#total quantity
m = df3['Quantity Counted'].sum()
print(m)
#%%
#grouping based on location
n = df3.groupby('Detailed Location').sum()

#%%
#difference
plt.bar(n.index, n['Difference'])
plt.xticks(rotation=60)
plt.xlabel('Plant Location')
plt.title('Difference for every plant')
plt.ylabel('Differnce in quantity counted vs expected')
#%%
b = df3.groupby('Counter').sum()
#%%
#counter
plt.bar(b.index, b['Difference'])
plt.xticks(rotation = 45)
plt.xlabel('Counters')
plt.ylabel('Difference for every plant')
plt.title('Discrepencies per counter')

#%%
#importing dataset 4
df4 = pd.read_excel(xls, 'Quantt')
#%%
df4.head()

#%%
#total cost
cost = df4['Total Cost'].sum()
print(cost)

#%%
#grouped based on description
total = df4.groupby('Description').sum()
print(total)
#%%
#cost of each material
plt.plot(total.index, total['Total Cost'], color='green')
plt.xticks(rotation = 90)
plt.xlabel('Item')
plt.ylabel('cost')
plt.title('cost per item')
plt.show()
#%%
#freight cost
plt.plot(total.index, total['Freight Cost'], color='red')
plt.xticks(rotation = 90)
plt.xlabel('Item')
plt.ylabel('Freight cost')
plt.title('Freight Cost per item')
plt.show()

#%%
#per unit cost
plt.plot(total.index, total['per unit'])
plt.xticks(rotation = 90)
plt.xlabel('type of product')
plt.ylabel('cost')
plt.title('per unit cost of each item')
#%%
#importinf data5
df5 = pd.read_excel(xls, 'Sales')

#%%
products = df5['Itemm'].value_counts()
print(products)
#%%
#total orders of each product
products.plot(kind='bar', figsize=(14,8))
plt.xlabel('item')
plt.ylabel('number of orders')
plt.title('total number of orders placed for each item')



#%%
#importing dataset for payroll
df6 = pd.read_excel(xls, 'Payroll')

#%%
#grouping based on employee type
gld = df6.groupby('Employee Type').mean()
print(gld)

#%%
#average pay per employee type
plt.plot(gld.index, gld['Pay'])
plt.xlabel('type of income')
plt.ylabel('income (in USD)')
plt.title('Income for each type')



#%%
#importing dataset 7
df7 = pd.read_excel(xls, 'per')
df7.head()

#%%
xxx = df7.groupby('Finished Items').sum()
print(xxx)

#%%
#per unit price
plt.bar(xxx.index, xxx['Suggested Distributor Price'])
plt.xticks(rotation = 90)
plt.xlabel('type of product')
plt.ylabel('per unit price')
plt.title('per unit price for each product')

























