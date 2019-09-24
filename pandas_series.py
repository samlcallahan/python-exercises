import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruits.describe()

fruits.unique()

fruits.value_counts()

fruits.mode()

fruits.value_counts().tail(1)

fruits[fruits.apply(len).idxmax()]

fruits[fruits.apply(len) > 5]

fruits.str.capitalize()

fruits.str.count("a")

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word.lower():
        count += letter in vowels
    return count

fruits.apply(count_vowels)

fruits[fruits.apply(lambda x: x.count("o") >= 2)]

fruits[fruits.apply(lambda x: "berry" in x)]

fruits[fruits.apply(lambda x: "apple" in x)]

fruits[fruits.apply(count_vowels).idxmax()]

prices = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

prices.describe() # object

def currency_to_float(string):
    return float(string[1:].replace(",",""))

prices = prices.apply(currency_to_float)

prices.max()
prices.min()

pd.cut(prices,4).value_counts()

binned = pd.cut(prices,4)

import matplotlib.pyplot as plt

histogram = prices.plot.hist(bins=4,title="Price Distribution")
histogram.set_xlabel("Price")

scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

scores.min()
scores.max()
scores.mean()
scores.median()

def num_to_letter_grade(score):
    letters = "FDCBA"
    ceiling = 60
    for i in range(5):
        if score < ceiling + (10 * i):
            return letters[i]

scores.apply(num_to_letter_grade)

def curve(pandas_series):
    to_add = 100 - pandas_series.max()
    return pandas_series.apply(lambda x: x + to_add)

curve(scores)

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

letters.mode()
letters.value_counts()[-1]

vowel_count = letters.isin(list("aeiou")).sum()

consonant_count = letters.size - letters.isin(list("aeiou")).sum()

letters.str.upper()

to_bar = letters.value_counts()[:6]

to_bar.plot.bar()