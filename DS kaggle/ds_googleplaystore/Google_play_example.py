import pandas as pd
#import numpy as np
#import seaborn as sns
#from sklearn import metrics
#import random
import matplotlib.pyplot as plt

df = pd.read_csv("googleplaystore.csv")
df.dropna(inplace=True) #удаление нулевых значений

# Cleaning Categories into integers
CategoryString = df["Category"]
categoryVal = df["Category"].unique()   # выделяем различные категории
categoryValCount = len(categoryVal)     #
# выдать каждой категории номер
category_dict = {}
for i in range(0,categoryValCount):
    category_dict[categoryVal[i]] = i
df["Category_c"] = df["Category"].map(category_dict).astype(int)    # добавил в df столец, соответствущий индексу категорий

def change_size(size):
    if 'M' in size:
        x = size[:-1]
        x = float(x) * 1000000
        return(x)
    elif 'k' in size:
        x = size[:-1]
        x = float(x) * 1000
        return(x)
    else:
        return None

df['Size'] = df['Size'].map(change_size)
#filling Size which had NA
df.Size.fillna(method = 'ffill', inplace = True)    # не понял, что делает

#Cleaning no of installs classification
df['Installs'] = [int(i[:-1].replace(',','')) for i in df['Installs']]

#Converting Type classification into binary
def type_cat(types):
    if types == 'Free': return 0
    else: return 1
df['Type'] = df['Type'].map(type_cat)

#Cleaning of content rating classification
# превращаешь все группы в числа (каждой группе свой id)
RatingL = df['Content Rating'].unique()
RatingDict = {}
for i in range(len(RatingL)):
    RatingDict[RatingL[i]] = i
df['Content Rating'] = df['Content Rating'].map(RatingDict).astype(int)

#Cleaning of genres
GenresL = df.Genres.unique()
GenresDict = {}
for i in range(len(GenresL)):
    GenresDict[GenresL[i]] = i
df['Genres_c'] = df['Genres'].map(GenresDict).astype(int)

#Cleaning prices
def price_clean(price):
    if price == '0':
        return 0
    else:
        price = price[1:]
        price = float(price)
        return price

# convert reviews to numeric
df['Reviews'] = df['Reviews'].astype(int)

print(df.info())

df['Price'] = df['Price'].map(price_clean).astype(float)

#dropping of unrelated and unnecessary items
df.drop(labels = ['Last Updated','Current Ver','Android Ver','App', 'Genres', 'Category'], axis = 1, inplace = True)
plt.figure()
plt.subplot(1,4,1)
df['Rating'].plot.box()
plt.subplot(1,4,2)
df['Size'].plot.box()
plt.subplot(1,4,3)
df['Reviews'].plot.box()
plt.subplot(1,4,4)
df['Installs'].plot.box()
plt.show()


print("Конец!")