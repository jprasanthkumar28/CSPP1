def count_option(a, options,options1):
	for i in range(len(options)):
		if i == a:
			if options in options1[i]:
				options1[i][options] += 1
	return options1

def main():
	q_count = int(input())
	dict1 = {}
	for i in range(q_count):
		question = str(input())
		options = []
	# while i < q_count:
		for x in range(4):
			options.insert(x,str(input()))
		dict1[question] = options
	# print(dict1)
	options = []
	for key in dict1:
		response = {}
		for value in dict1[key]:
			response[value] = 0
		options.append(response)
	# print(options)
	parti_count = int(input())
	for x in range(parti_count):
		p_name = input()
		for i in range(q_count):
			string = input().split()
			options1 = count_option(int(string[0]) - 1,string[1],options)
	final = []
	for x in options1:
		maxi = max(x.values())
		for val in x:
			if x[val] == maxi:
				final.append(val)
	i = 0
	for key in dict1:
		print("Highest number of votes for question:"+ key + ":" + final[i])
		i = i + 1
		if i == q_count:
			break

	# print(options1)

if __name__ == '__main__':
	main()