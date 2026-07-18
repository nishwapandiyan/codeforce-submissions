import sys
input = sys.stdin.readline
 
def main():
      a = int(input())
      b = int(input())
      c = int(input())
 
      print(max(
          a + b + c,
          a * b * c,
          (a + b) * c,
          a * (b + c),
          a + b * c,
          a * b + c
      ))
if __name__ == "__main__":
    main()    