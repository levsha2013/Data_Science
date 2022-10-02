import pandas as pd
from statsmodels import robust
from collections import defaultdict

table = pd.read_csv('googleplaystore.csv')
category_count = defaultdict(int)
for i in table['Category']:
    category_count[i] += 1
print(category_count)

type_count = defaultdict(int)
for i in table['Type']:
    type_count[i] += 1

year = defaultdict(int)
for i in table['Last Updated']:
    if type(i) != str:
        print(i)
    else:
        year[i.split(",")[-1]] += 1



for i in table1.keys():
    print(f'\t{i}')
    if type(table[i][1]) != str:
        print(table[i].mean())
        print(f"медиана - {table[i].median()}")
        print(f"стандартное отклонение - {table[i].std()}")
        print(f"робастная оценка медианного абсолютного значение - {robust.scale.mad(table[i])}")
        print(f"межквартильный размех (0.75-0.25) - {table[i].quantile() - table[i].quantile()}")
