import sys
 
input = sys.stdin.readline
 
def main():
    c = input()
    cards = list(map(str,input().split()))
    for card in cards:
        if card[0] == c[0] or card[1] == c[1]:
            print("YES")
            break
    else:
        print("NO")
 
if __name__ == "__main__":
    main()