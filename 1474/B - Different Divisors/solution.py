import sys
 
input = sys.stdin.readline
 
def is_prime(x):
    if x < 2:
        return False
 
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
 
    return True
 
def main():
    t = int(input())
 
    for _ in range(t):
        d = int(input())
 
        p = d + 1
        while not is_prime(p):
            p += 1
 
        q = p + d
        while not is_prime(q):
            q += 1
 
        print(p * q)
 
if __name__ == "__main__":
    main()