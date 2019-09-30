with open('/usr/share/dict/words') as f:
    words = f.read().strip().split('\n')

import pandas as pd

def follows_rule(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    ought_sum = letters.find(word[0].lower()) + 1
    actual_sum = 0
    for letter in word[1:]:
        actual_sum += letters.find(letter.lower()) + 1
    return (ought_sum == actual_sum) and len(word) == 5

results = []
for i in words:
    results.append(follows_rule(i))

words = pd.Series(words)
print(words[results])