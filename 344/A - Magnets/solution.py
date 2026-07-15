from itertools import groupby
n = int(input())
magnets = [input() for _ in range(n)]
print(len(list(groupby(magnets))))