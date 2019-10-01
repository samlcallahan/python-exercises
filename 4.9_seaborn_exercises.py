import seaborn as sns
from pydataset import data
import pandas as pd
import matplotlib.pyplot as plt
from env import host, password, user

iris = data('iris')
sns.distplot(iris['Petal.Length'])

sns.regplot(x='Petal.Length', y='Petal.Width', data=iris) # Yes

sns.relplot(x='Sepal.Length', y='Sepal.Width', data=iris, hue='Species') # Probably? Many edge cases between versicolor and virginica

sns.pairplot(iris) # It looks like setosa is easy to identify regardless of feature; I think petal width/length look like the best pair of features by which to distinguish versicolor and virginica, but it's still an imperfect metric.

anscombe = sns.load_dataset('anscombe')

anscombe.groupby('dataset').describe()

sns.relplot(x='x',y='y', data=anscombe, col='dataset')

insectsprays = data('InsectSprays')

sns.boxplot(data=insectsprays, y='count', x='spray')

swiss = data('swiss')

swiss['is_catholic'] = swiss['Catholic'] > 80

sns.catplot(x='is_catholic', y='Fertility', data=swiss) # Catholicism correlates with higher fertility

swiss.drop('is_catholic', axis=1)
sns.heatmap(swiss.corr(), cmap='vlag') # Education

def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

url = get_db_url(user, host, password, 'chipotle')
query = 'select * from orders'
chipotle = pd.read_sql(query,url)

chipotle['price'] = chipotle['item_price'].apply(lambda x: float(x[1:]))
revenues = chipotle.groupby('item_name')['price'].sum().sort_values()
top_revenues = pd.Series(revenues.tail(4))
to_bar = pd.DataFrame()
to_bar['item'] = top_revenues.index
to_bar['revenue'] = top_revenues.values
sns.barplot(x='item', y='revenue', data=to_bar)

sleep = data('sleepstudy')
sleep['Subject'] = 'subject_' + sleep['Subject'].astype(str)
sns.set_style('dark')
sns.set_context(font_scale=.5,rc={"grid.linewidth": .5, "axes.linewidth": .5, "ytick.major.width": .5, "xtick.major.width": .5,"lines.linewidth": 0.5})
sns.lineplot(x='Days', y='Reaction', hue='Subject', data=sleep)
sns.set_context(rc={"lines.linewidth": 4})
sns.lineplot(x='Days', y='Reaction', data=sleep, ci=None)
sns.despine()
plt.show()