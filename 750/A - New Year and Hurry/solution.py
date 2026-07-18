import sys
 
input = sys.stdin.readline
 
def main():
    n,k = map(int,input().split())
    time = 240 - k
    count = 0
    for i in range(1,n+1):
        if i*5 <= time:
            time -= i*5
            count += 1
        else:
            break
    print(count)
 
if __name__ == "__main__":
    main()