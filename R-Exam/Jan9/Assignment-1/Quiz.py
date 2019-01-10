def load_ques(data):
	global ques
	print("|----------------|")
	print("| Load Questions |")
	print("|----------------|")
	q_count = int(data[1])
	flag = True
	# print(q_count)
	for i in range(q_count):
		ques.append(input().split(":"))
	# print(ques)
	if ' ' in ques:
		print("Error! Malformed question")
		flag = False
	elif q_count == 0:
		print("Quiz does not have questions")
	elif flag != False: 
		print(q_count,"are added to the quiz")

def start_quiz(data):
	print("|------------|")
	print("| Start Quiz |")
	print("|------------|")
	option = int(data[1])
	for q in ques:
		ans = input().split(" ")
		# print(ans)
		q.append(ans[1])
		# print(q)
		print(q[0],"(",q[3],")")
		option = q[1].split(",")
		print(option[0],"\t",option[1],"\t",option[2],"\t",option[3])
		print()

def display(data):
	print("|--------------|")
	print("| Score Report |")
	print("|--------------|")
	# print("Hiiiiiiiiiiiiiii")
	totalscore = 0
	for q in ques:
		print(q[0])
		if q[2] == q[5]:
			print("Correct Answer! - Marks awarded:",q[3])
			totalscore += int(q[3])
		else:
			print("Wrong Answer! - Penality:", q[4])
			totalscore += int(q[4])
	print("Total Score",totalscore)

def main():
	global ques
	ques = []
	while True:
		try:
			line = input().split(" ")
		except EOFError:
			break
		# print(q_count)
		if line[0] == "LOAD_QUESTIONS":
			load_ques(line)
		elif line[0] == "START_QUIZ":
			start_quiz(line)
		else:
			display(line)

		
if __name__ == '__main__':
	main()