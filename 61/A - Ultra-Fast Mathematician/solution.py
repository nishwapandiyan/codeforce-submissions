import sys
input = sys.stdin.readline
 
def main():
    s = input()
    r = input()
    res = ""
    for i in range(len(s)-1):
        if s[i] == r[i]:
            res += '0'
        else:
            res += '1'
    print(res)
 
if __name__ == "__main__":
    main()