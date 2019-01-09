from collections import Counter
def winner(data):
	# print(data)
	# data = list(data)
	# string = ""
	# for x in data:
	#     string += ''.join(str(x))
	# print(string)
	# for i in range(len(string)):
	# 	index = string.index('1')
		# print(index)

	# for value in data:
		# print(type(value))
	res1 = []
	ques1 = {}
	ques2 = {}
	ques3 = {}
	value = Counter(data)
	# print(value)
	for key,val in value.items():
		# print(key,val)
		# ans = max(value.values())
		# res1.append(key)
		# res1.append(val)
		if '1' == key[0]:
			ques1.update({key[1:]:val})
			# print(max(ques1.values()))
		elif '2' == key[0]:
			ques2.update({key[1:]:val})
		elif '3' == key[0]:
			ques3.update({key[1:]:val})

	lst1 = []
	for k,v in ques1.items():
		lst1.append(v)
	for x in ques1:
		if ques1[x] == max(lst1):
			print("Highest number of votes for question : Who should be the next Prime Minister? :"+x)
	lst2 = []
	if len(ques2) != 0:
		for k,v in ques2.items():
			lst2.append(v)
		for x in ques2:
			if ques2[x] == max(lst2):
				print("Highest number of votes for question : Who will be the next cm for Telangana? :"+x)
	lst3 = []
	if len(ques3) != 0:
		for k,v in ques3.items():
			lst3.append(v)
		for x in ques3:
			if ques3[x] == max(lst3):
				print("Highest number of votes for question : Who will be the next cm for AP? :"+x)
	# result = {1:ques1, 2:ques2, 3:ques3}
	# return result
	# print(result)
	# print(ques1)
	# print(ques2)
	# print(ques3)

	# print(ques1,ques2,ques3)

def main():
	q_count = int(input())
	parti = []
	data = []
	# i = 0
	for i in range(q_count):
		question = str(input())
		options = []
	# while i < q_count:
		for x in range(4):
			options.insert(x,str(input()))
		data.append(question)
		data.append(options)
	# print(data)
		# print(question)
		# print(options)
	# i = i + 1 
	parti_Count = int(input())
	p_option = []
	for j in range(parti_Count):
		p_name = str(input())
		for k in range(q_count):
			p_option.insert(k,input())
		# p_option.append(p_name)
	# print(data, p_option)
	winner(p_option)
	# for x in range(1,4):
	# 	if x == 1:
	# 		data.append(res)

	# print(data)

if __name__ == '__main__':
	main()