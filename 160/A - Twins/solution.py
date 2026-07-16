n = int(input())
coins = sorted(list(map(int,input().split())),reverse =  True)
total = sum(coins)
count = 0
cur = 0
for val in coins:
    count += 1
    total -= val
    cur += val
    if cur > total:
        print(count)
        break