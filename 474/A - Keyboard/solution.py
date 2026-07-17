import sys
 
input = sys.stdin.readline
 
def main():
    k = input().strip().upper()
    s = input().strip()
 
    key = "qwertyuiopasdfghjkl;zxcvbnm,./"
 
    res = ""
 
    for i in s:
      if k == 'R':
        res += key[key.index(i)-1]
      if k == 'L':
        res += key[key.index(i)+1]
 
    print(res)
if __name__ == "__main__":
    main()