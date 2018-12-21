def main():
	dict1 = {}
	total = 0
	for _ in range(int(input())):
		list1 = input().split()
		if int(list1[0]) in dict1.keys():
			if int(list1[2]) == 1:
				total += int(list1[1])
				num = dict1[int(list1[0])]
				dict1[int(list1[0])] = num + int(list1[1])
			elif int(list1[2]) == 0:
				total -= int(list1[1])
				num = dict1[int(list1[0])]
				dict1[int(list1[0])] = num - int(list1[1])
		else:
			if int(list1[2]) == 1:
				total += int(list1[1])
				dict1[int(list1[0])] = int(list1[1])
	print(total)
	print([k for k in dict1.keys() if dict1[k] == max(dict1.values())])

main()