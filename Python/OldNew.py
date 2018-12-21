# Write a java program to replace each element of the given char array that matches the given character with the given replacement.
# Sample Input:
# m u r t h y
# y
# i

listt = list(input())
old = input()
ne = input()
for i in range(len(listt)):
    if listt[i] == old:
       	listt[i] = ne
print(listt)
