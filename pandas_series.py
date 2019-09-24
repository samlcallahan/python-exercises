import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

fruits.describe()

fruits.unique

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