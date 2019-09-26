import numpy as np
import pandas as pd
from pydataset import data
from env import user, host, password

mpg = data('mpg')

mpg["overall"] = mpg[["hwy","cty"]].mean(axis=1)
mpg.groupby('manufacturer')['overall'].mean().idxmax()

mpg['manufacturer'].unique().size

mpg['model'].unique().size

mpg['transmission'] = mpg['trans'].apply(lambda x: "man" if "man" in x else "auto")
mpg.groupby('transmission')['overall'].mean().idxmax()

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

users.merge(roles,how='right',left_on='role_id',right_on='id') # lists all roles at least once, repeats if there are mutliple people with that role
users.merge(roles,how='outer',left_on='role_id',right_on='id') # lists all roles and users at least once, even if there are no roles for that person or no people with that role
users.merge(roles, how='outer') # appears to just stack the tables on one another

def get_db_url(username, hostname, password, db_name):
    return f'mysql+pymysql://{username}:{password}@{hostname}/{db_name}'

query = 'select * from employees'

employees = pd.read_sql(query,get_db_url(user,host,password,'employees'))