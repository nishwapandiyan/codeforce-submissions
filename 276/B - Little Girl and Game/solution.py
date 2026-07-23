import sys
from collections import Counter
 
input = sys.stdin.readline
 
def main():
    s = input().strip()
    freq = Counter(s)
    odd = 0
    for count in freq.values():
        if count % 2 == 1:
            odd += 1
    if odd == 0 or odd % 2 == 1:
        print("First")
    else:
        print("Second")
 
if __name__ == "__main__":
    main()