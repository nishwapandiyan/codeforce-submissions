s = input().lower()
vowel = "aeiouy"
for ch in s:
    if ch not in vowel:
        print("."+ch,end='')