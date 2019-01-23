def doTask(data):
	# print(data)
	strr = ""
	strr = data[1] + ", " + data[2] + ", " + data[3]
	if data[4] == 'y':
		strr += ", Important"
	else:
		strr += ", Not Important"
	if data[5] == 'y':
		strr += ", Urgent"
	else:
		strr += ", Not Urgent"
	if data[6] == "todo" or data[6] == "done":
		strr += ", "+data[6]
	else:
		strr = "Invalid status dud"
	print(strr)


def main():
	string = input().split(",")
	if string[0] == "task":
		doTask(string)

if __name__ == '__main__':
	main()