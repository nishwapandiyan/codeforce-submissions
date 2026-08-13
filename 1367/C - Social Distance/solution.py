import sys
 
def solve():
    # Read all tokens from standard input for fast execution
    input_data = sys.stdin.read().split()
    if not input_data:
        return
 
    t = int(input_data[0])
    idx = 1
 
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        s = input_data[idx+2]
        idx += 3
 
        ans = 0
        # Initialize distance as a large number to simulate no '1' on the left
        last_one = -float('inf')
 
        # Precompute next '1' positions for quick right-side boundary checks
        next_one = [float('inf')] * n
        curr_next = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                curr_next = i
            next_one[i] = curr_next
 
            # Greedy placement
        for i in range(n):
            if s[i] == '1':
                last_one = i
            else:
                # Check if it satisfies the distance k for both left and right sides
                if (i - last_one > k) and (next_one[i] - i > k):
                    ans += 1
                    last_one = i # Mark this spot as occupied
 
        out.append(str(ans))
 
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()