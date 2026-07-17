import sys
input = sys.stdin.readline
 
def main():
    n = int(input())
    cards = list(map(int,input().split()))
    ser = 0
    dim = 0
 
    l = 0
    r = n-1
 
    turn = 0
    while l <= r:
        if cards[l] > cards[r]:
            temp = cards[l]
            l += 1
        else:
            temp = cards[r]
            r -= 1
 
        if turn % 2 == 0:
            ser += temp
        else:
            dim += temp
        turn += 1
 
    print(ser,dim)
 
if __name__ == "__main__":
    main()