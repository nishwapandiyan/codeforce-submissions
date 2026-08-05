import sys
 
def solve():
 
    input = sys.stdin.read
    data = input().split()
 
    if not data:
        return
 
    iterator = iter(data)
    t = int(next(iterator))
 
    out = []
    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
 
        # Parse multiset S
        S = [int(next(iterator)) for _ in range(n)]
        # Parse multiset T
        T = [int(next(iterator)) for _ in range(n)]
 
        base_S = []
        base_T = []
 
 
        for x in S:
            rem = x % k
            base = min(rem, (k - rem) % k)
            base_S.append(base)
 
        for y in T:
            rem = y % k
            base = min(rem, (k - rem) % k)
            base_T.append(base)
 
        base_S.sort()
        base_T.sort()
 
        if base_S == base_T:
            out.append("YES")
        else:
            out.append("NO")
 
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()