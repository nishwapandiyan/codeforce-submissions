import sys
 
data = list(map(int, sys.stdin.read().split()))
 
n = data[0]
k = data[1]
scores = data[2:]
 
cutoff = scores[k - 1]
count = sum(score > 0 and score >= cutoff for score in scores)
 
print(count)