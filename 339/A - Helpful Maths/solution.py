s = input()
lst = sorted([x for x in s if x.isdigit()])
print('+'.join(lst))