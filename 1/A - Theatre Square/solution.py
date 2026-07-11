import math
floor = list(map(int,input().split()))
l,w,a = floor
length = (l+a-1) // a
width = (w+a-1) // a
print(length * width)