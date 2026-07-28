import sys
 
input = sys.stdin.readline
 
def main():
    s1 = input().strip()
    s2 = input().strip()
    target = 0
    for ch in s1:
        if ch == '+':
            target += 1
        else:
            target -= 1
 
    current = 0
    q = 0
 
    for ch in s2:
        if ch == '+':
            current += 1
        elif ch == '-':
            current -= 1
        else:
            q += 1
 
    success = 0
    total = 2**q
 
    def dfs(idx,pos):
        nonlocal success
 
        if idx == q:
            if pos == target:
                success += 1
            return
        dfs(idx+1,pos+1)
        dfs(idx+1,pos-1)
    dfs(0,current)
    print(f"{success/total:.12f}")
 
if __name__ == "__main__":
    main()