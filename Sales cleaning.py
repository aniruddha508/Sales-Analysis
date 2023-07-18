import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Diwali Sales Data.csv",encoding= 'unicode_escape')
df.drop(['Status','unnamed1'],axis=1,inplace=True)
# print(df.info())
df.dropna(inplace=True)
df['Amount']=df['Amount'].astype=('int')
df.rename(columns={'Marital_Status':'Shaadi'})

# bar graph gender
# ax = sns.countplot(x = 'Gender',data = df)
# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

# plotting a bar chart for gender vs total amount
# sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).astype=('int')
# sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
# plt.show()

# # plotting age groupplot
# plt.figure(figsize=(10,7))
# bx=sns.countplot(x="Age Group",data=df,hue='Gender')


# #total amount vs group age
# sales=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).astypr=('int')
# sns.countplot(x='Age Group',data=sales,hue="Gender")

# # total orders vs states top 10
# plt.figure(figsize=(15,5))
# sales_1=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(5)
# sns.barplot(x='State',y='Orders',data=sales_1)
# plt.xticks(rotation=45)


# # total amount/sales vs top 10 states
# sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
# sns.barplot(data = sales_state, x = 'State',y= 'Amount')

# maretaial status
# ax = sns.countplot(data = df, x = 'Marital_Status')
# sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')

# ocupation
# ax = sns.countplot(data = df, x = 'Occupation')
# sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

# product category
# ax = sns.countplot(data = df, x = 'Product_Category')
# sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
# sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
# plt.show()
# sns.pairplot(df,hue='Gender',palette='rocket')
# plt.show()