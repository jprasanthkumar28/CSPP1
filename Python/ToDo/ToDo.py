def doTask(data):
	# print(data)
	strr = ""
	if data[1] == '':
		strr = "Title not provided"
	else:
		strr = data[1] + ", " + data[2] + ", "
	if int(data[3]) < 0:
	 	strr = "Invalid timeToComplete -1"
	else:
		strr += data[3]
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