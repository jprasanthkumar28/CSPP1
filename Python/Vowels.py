# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print
# Number of vowels: 5

st = input()
# st = "azcbobobegghakl"
count = 0
for char in st:
	if char in('a', 'e', 'i', 'o', 'u'):
	    count += 1
print(count)
