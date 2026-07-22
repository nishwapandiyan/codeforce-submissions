import sys
 
input = sys.stdin.readline
 
def main():
        n = int(input())
        arr = list(map(int,input().split()))
        s_arr = sorted(arr)
 
 
        pre1 = [0]
        for x in arr:
            pre1.append(pre1[-1] + x)
        pre2 = [0]
        for x in s_arr:
            pre2.append(pre2[-1]+x)
 
        t = int(input())
        for _ in range(t):
            v,l,r = map(int,input().split())
            if v == 1:
                print(pre1[r] - pre1[l-1])
            if v == 2:
                 print(pre2[r] - pre2[l-1])    
 
if __name__ == "__main__":
    main()