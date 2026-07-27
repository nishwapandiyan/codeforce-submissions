import sys
 
input = sys.stdin.readline
 
def main():
    n,k = map(int,input().split())
    ans = []
    mp = {}
    for _ in range(k):
        a, b = map(str,input().split())
        mp[a] = b
    s = input().split()
    for word in s:
        if len(mp[word]) < len(word):
            ans.append(mp[word])
        else:
            ans.append(word)
    print(*ans)
if __name__ == "__main__":
    main()