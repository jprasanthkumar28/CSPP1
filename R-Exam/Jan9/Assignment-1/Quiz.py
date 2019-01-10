def load_ques(data):
	global ques
	global flag
	flag = 0
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	# q_count = int(data[1])
	# print(q_count)
	for i in range(q_count):
		ques.append(input().split(":"))
	# print(ques)
	for item in ques:
		if '' in item:
			print("Error! Malformed question")
			flag = 1
		elif int(item[1]) == 0:
			print("Quiz does not have questions")
			flag = 1
		elif flag != 1: 
			print(q_count,"are added to the quiz")

def start_quiz(data):
	# global flag
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	option = int(data[1])
	for q in ques:
		if flag == 0:
			ans = input().split(" ")
			# print(ans)
			q.append(ans[1])
			# print(q)
			print(q[0],"(",q[3],")")
			option = q[1].split(",")
			print(option[0],"\t",option[1],"\t",option[2],"\t",option[3])
			print()
		break

def display(data):
	# global flag
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	# print("Hiiiiiiiiiiiiiii")
	totalscore = 0
	for q in ques:
		if flag == 0:
			print(q[0])
			if q[2] == q[5]:
				print("Correct Answer! - Marks awarded:",q[3])
				totalscore += int(q[3])
			else:
				print("Wrong Answer! - Penality:", q[4])
				totalscore += int(q[4])
		print("Total Score",totalscore)
		break

def main():
	# global flag
	# flag = 0
	global ques
	ques = []
	while True:
		try:
			line = input().split(" ")
		except EOFError:
			# print("Hiiiiiiiiiiiiiii")
			break
		# print(q_count)
		if line[0] == "LOAD_QUESTIONS":
			load_ques(line)
		elif line[0] == "START_QUIZ":
			start_quiz(line)
		elif line[0] == "SCORE_REPORT":
			display(line)

		
if __name__ == '__main__':
	main()