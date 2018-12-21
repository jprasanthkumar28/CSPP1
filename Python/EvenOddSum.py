s = input()
length = len(s)
even = ""
odd = ""
if length == 0:
	# result = 0
	for i in range(0,length,1):
		result += s[i] + s[length]
		length-1;
	print(result)