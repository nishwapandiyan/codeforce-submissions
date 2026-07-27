import sys
 
input = sys.stdin.readline
 
def main():
    old = input()
    new = input()
    s = input()
 
    mp = {}
    for i in range(26):
        mp[old[i]] = new[i]
        # print(mp)
 
    res = ""
 
    for ch in s:
        if ch.isnumeric():
            res += ch
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
                res += mp[ch].upper()
            else:
                res += mp[ch]
    print(res)
 
if __name__ == "__main__":
    main()