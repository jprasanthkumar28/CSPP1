def main():
	# while True:
	wall = {}
	string = input()
	wallets = int(input())
	for x in range(wallets):
		val = input()
		if val not in wall:
			wall[val] = 1000
		
		# print(val)
	nextval = input()
	if nextval == "debit":
		data = input().split(" ")
		for key,val in wall.items():
			if data[0] == key:
				if int(data[1]) > val:
					print("Insufficient funds")
					print(data[1])
					print("Thank you")
					break
				# print(data[0])
			# lst = []
			# lst = key
			# if data[0] in lst:
			# 	print(data[0])
			# print(lst)
	# wallet = input()
	# nextval = input()

	# else:
	# 	if nextval == "debit":
	# print(nextval)
	# print(wall)
	# print(data)
		

if __name__ == '__main__':
	main()