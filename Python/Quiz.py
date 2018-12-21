def main():
	while True:
		case_input = input()
		if case_input:
			case_input = case_input.split(" ")
			if case_input[0]=="LOAD_QUESTIONS":
				load_questions(case_input)
				pass
			elif case_input[0]=="START_QUIZ":
				start_quiz(case_input)
				pass
			else:
				display_score_report(case_input)
				pass
		else:
			break

questions_objects = []
def load_questions(case_input):
	print('load_questions')
	questions_count = int(case_input[1])
	for i in range(0,questions_count):
		questions_objects.append(input().split(":"))
	if questions_count > 1:
		print(questions_count, "are added to quiz")
	else:
		print("no questions are added")
	#print(questions_objects)

def start_quiz(case_input):
	print('start_quiz')
	choice_count = int(case_input[1])
	for questions_obj in questions_objects:
		answers = input().split(" ")
		questions_obj.append(answers[1])
		#print(questions_obj)
		print(questions_obj[0],"(",questions_obj[3],")")
		choice = questions_obj[1].split(",")
		print(choice[0],"   ",choice[1],"   ",choice[2],"   ",choice[3])
	#display_score_report(questions_obj)
	#print()
	pass

def display_score_report(questions_obj):
	print('display_score_report')
	totalScore = 0
	for questions_obj in questions_objects:
		print(questions_obj[0])
		if questions_obj[2]==questions_obj[5]:
			print("correct Answer!- Marks Awarded: ",questions_obj[3])
			totalScore = totalScore + int(questions_obj[3]);
		else:
			print("wrong Answer! - Penalty: ",questions_obj[4])
			totalScore = totalScore + int(questions_obj[4]);
	print("Total Score", totalScore)
	pass

main()