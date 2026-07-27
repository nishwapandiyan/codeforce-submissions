import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    arr = list(map(str,input().split()))
    zc = arr.count('0')
    fc = arr.count('5')
 
    if zc == 0:
        print(-1)
    elif fc < 9:
        print(0)
    else:
        rem = (fc // 9) * 9
        print('5'*rem + '0'*zc)
if __name__ == "__main__":
    main()