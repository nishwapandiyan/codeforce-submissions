import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input())
    count = 0
    notes = [100,20,10,5,1]
    for note in notes:
        count += n // note
        n %= note
    print(count)
if __name__ == "__main__":
    main()