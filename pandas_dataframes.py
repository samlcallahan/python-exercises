import pandas as import pd
from pydataset import data
import numpy as np

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

df["passing_english"] = df["english"] >= 70

df.sort_values('passing_english') # duplicates sorted by id

df.sort_values(['passing_english','name'])

df.sort_values(['passing_english','english'])

df["overall"] = df[["math","english","reading"]].mean(axis=1)

mpg = data('mpg')

rows, columns = mpg.shape

mpg.dtypes

mpg.describe()
mpg.info()

mpg.rename(columns={'cty':"city"},inplace=True)

mpg.rename(columns={'hwy':'highway'},inplace=True)

mpg[mpg["city"] > mpg["highway"]] # no

mpg["mileage_difference"] = mpg["highway"] - mpg["city"]
mpg.sort_values("mileage_difference")

max_diff = mpg["mileage_difference"].max()
mpg[mpg["mileage_difference"] == max_diff]

compacts = mpg["class"] == "compact"
id_min = mpg[compacts]["highway"].idxmin()
id_max = mpg[compacts]["highway"].idxmax()
mpg["manufacturer"][id_min] + " " + mpg["model"][id_min]
mpg["manufacturer"][id_max] + " " + mpg["model"][id_max]

mpg["average_mileage"] = mpg[["highway","city"]].mean(axis=1)

dodge = mpg["manufacturer"] == "dodge"
id_min = mpg[dodge]["average_mileage"].idxmin()
id_max = mpg[dodge]["average_mileage"].idxmax()
mpg["manufacturer"][id_min] + " " + mpg["model"][id_min]
mpg["manufacturer"][id_max] + " " + mpg["model"][id_max]

mammals = data('Mammals')

rows, columns = mammals.shape

mammals.dtypes

mammals.info()
mammals.describe()

fastest_id = mammals["speed"].idxmax()
mammals["weight"][fastest_id]

mammals["specials]"].sum()/mammals.size

median_speed = mammals["speed"].median()
faster_than_median = mammals["speed"] > median_speed
hoppers_faster_than_median = mammals[faster_than_median]["hoppers"].sum()
hoppers_faster_than_median / mammals.size