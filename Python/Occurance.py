s = input()
count = 0
for i in range(len(s) - 2):
	if s[i] + s[i+1] + s[i+2] == 'bob':
		count += 1
print(count)


# s = [['561', 10, 5], ['562', 110, 53]].split()
# # diff = s[1] - s[2]

# print(s)