import numpy as np
import pandas as pd
from pydataset import data
from env import user, host, password
import matplotlib as plt

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
url = get_db_url(user,host,password,'employees')

employees = pd.read_sql(query,url)

pd.read_sql(query + "234",get_db_url(user,host,password,'employees')) # this database doesn't exist bc we're calling employees234
pd.read_sql(query,get_db_url(user,host,password,'employees') + '/asdf') # access denied to database employees/asdf

query = 'select * from titles'

titles = pd.read_sql(query,url)

title_counts = titles.groupby('title')['emp_no'].count()
values = title_counts.values
title_list = title_counts.index
plt.bar(title_list, values)
plt.xticks(rotation=30)
plt.title("Number of Employees with Each Title")
plt.show()

joined = employees.join(titles.set_index('emp_no'),on='emp_no')
mask_current = joined['to_date'].apply(lambda x: '9999' not in str(x))
changed = joined[mask_current]
changed["diff"] = changed["to_date"] - changed["from_date"]
plt.hist(changed['diff'].apply(lambda x: x.days/365),bins=6)
plt.xlabel('Years')
plt.ylabel('# of Employees')
plt.title('Frequency of Job Changes')
plt.show()

joined.groupby('title')['hire_date'].max()

query='''
    select * from titles
	join dept_emp
	using(emp_no)
	join departments
	on dept_emp.dept_no=departments.dept_no;
    '''
titles_dept = pd.read_sql(query,url)
titles_dept.groupby('dept_name')['title'].unique().apply(len)

query = 'select * from orders'
url = get_db_url(user,host,password,'chipotle')
chipotle = pd.read_sql(query,url)
chipotle['price'] = chipotle['item_price'].apply(lambda x: float(x[1:]))
chipotle.groupby('order_id')['price'].sum()

chipotle.groupby('item_name')['item_price'].count().sort_values().tail(3)
chipotle.groupby('item_name')['price'].sum().idxmax()