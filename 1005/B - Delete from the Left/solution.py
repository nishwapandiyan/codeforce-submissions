import sys
 
input = sys.stdin.readline
 
def main():
    s1 = input()
    s2 = input()
    
    l = len(s1)-1
    r = len(s2)-1
    
    ct = 0
    while l >= 0 and r >= 0 and s1[l] == s2[r]:
        ct += 1
        l -= 1
        r -= 1
    print(len(s1)-ct + len(s2)-ct)    
 
if __name__ == "__main__":
    main()