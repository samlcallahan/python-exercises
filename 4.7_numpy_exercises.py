import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

negative_count = len(a[a < 0])

positive_count = len(a[a > 0])

positive_and_even = ((a > 0) & (a % 2 ==0)).sum()

b = a + 3
positive_plus_three = len(b[b > 0])

squared = a ** 2
mean = squared.mean()
std_dev = squared.std()

centered = a - a.mean()

z_scores = centered / a.std()