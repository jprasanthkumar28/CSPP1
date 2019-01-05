def total(lst):
	sum1 = 0
	for value in lst:
		try:
			if type(value) != str:
				sum1 += value
		except TypeError:
			sum1 += total(value)
	return sum1

def count(lst):
	# result = lst.split("]")
	c = 0
	string = ""
	string = ''.join(str(e) for e in lst)
	# 	string += lst[i]
	# print(string)
	for i in range(len(string)):
		if string[i] == '[':
			c += 1
	return c

def main():
	# lst = []
	# sum1 = 0
	data = eval(input())
	print(total(data))
	print(count(data))
	# for value in data:
	# 	if ']' != value or '[' != value:
	# 		sum1 += value
	# 	# for x in value:
	# 		# print(value)




if __name__ == '__main__':
	main()