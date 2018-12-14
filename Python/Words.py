# Reverse of three characters in the given string

s = input()
# s = "abcdefghijk"
res = ""
for i in range(0, len(s), 3):
       words = s[i : i+3]
       # print(words)
       newWords = words[ : : -1]
       res = res +" "+ newWords
print(res)