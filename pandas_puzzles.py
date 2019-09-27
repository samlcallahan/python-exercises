import pandas as pd

pd.__version__

pd.show_versions()

import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data,index=labels)

df.info()

df.head(3)

df[['animal','age']]

df[['animal','age']].iloc[[3,4,8]]

df[df['visits'] > 3]

df[df['age'] == df['age']]

df[(df['age'] < 3) & (df['animal'] == 'cat')]

df[df['age'].between(2,4)]

df.loc['f','age'] = 1.5

df['visits'].sum()

df.groupby('animal')['age'].mean()

new_row = ['okapi', 9, 10, 'no']

df.loc['k'] = new_row
df = df.drop('k')

df.groupby('animal')['visits'].count()
df['animal'].value_counts() # alt solution

df.sort_values(['age','visits'],ascending=[False,True])

df['priority'] = df['priority'].map({'yes': True, 'no': False})

df['animal'] = df['animal'].map({'snake': 'python'})

df['animal'] = df['animal'].apply(lambda x: 'python' if x == 'snake' else x)
df['animal'] = df['animal'].replace('snake', 'python') # alt solution

df.pivot_table(index='animal',columns='visits',values='age',aggfunc='mean')

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
df[df['A'].shift() != df['A']]

df = pd.DataFrame(np.random.random(size=(5, 3)))
df.sub(df.mean(axis=1), axis=0)

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
df.sum().idxmin()

len(df.drop_duplicates(keep=False))

df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)

