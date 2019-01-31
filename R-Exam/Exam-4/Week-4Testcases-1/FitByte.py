
def main():
    arr = [2,2,3,4,4,5,5]
    dup = set(arr)
    res = {}

    for i in dup:
        res = arr.count(i)
        print(i, res)
if __name__ == "__main__":
    main()

# def main():
# 	noOfiter = int(input())
# 	i = 0
# 	global dict1
# 	dict1 = {}
# 	listfood = []
# 	listwater = []
# 	listactivity = []
# 	listweight = []
# 	listsleep = []
# 	loglist = ['Foodlog', 'Waterlog', 'PhysicalActivitylog', 'Weightlog', 'Sleeplog', 'Summary']
# 	for i in range(noOfiter):
# 		log = input()
# 		if log not in loglist:
# 			log1 = log.split(" ")
# 			if log1[0] == 'Food':
# 				listfood.append(log1[1])
# 				foodlog(log1[0], listfood)
# 			if log1[0] == 'Water':
# 				listwater.append(log1[1])
# 				waterlog(log1[0], listwater)
# 			if log1[0] == 'PhysicalActivity':
# 				listactivity.append(log1[1])
# 				activitylog(log1[0], listactivity)
# 			if log1[0] == 'Weight':
# 				listweight.append(log1[1])
# 				weightlog(log1[0], listweight)
# 			if log1[0] == 'Sleep':
# 				# print("Heeeeeerak")
# 				listsleep.append(log1[1])
# 				# print("helloooooooo")
# 				# print(listsleep)
# 				sleeplog(log1[0], listsleep)
# 		# print(items)
# 		# print(log)
# 		if log == "Foodlog":
# 			prin(dict1, 'Food')
# 		if log == "Waterlog":
# 			prin(dict1, 'Water')
# 		if log == "PhysicalActivitylog":
# 			prin(dict1, 'PhysicalActivity')
# 		if log == "Weightlog":
# 			prin(dict1, 'Weight')
# 		if log == "Sleeplog":
# 			prin(dict1, 'Sleep')
# 		if log == "Summary":
# 			priin(dict1)
# 	# print(dict1)
# 	# val = dict1.values()
# 	# print(val)

# def foodlog(item, listfood):
# 	global dict1
# 	dict1[item] = listfood
# 	return dict1

# def waterlog(item, listwater):
# 	global dict1
# 	dict1[item] = listwater
# 	return dict1

# def activitylog(item, listactivity):
# 	global dict1
# 	dict1[item] = listactivity
# 	return dict1

# def weightlog(item, listweight):
# 	global dict1
# 	dict1[item] = listweight
# 	return dict1

# def sleeplog(item, listsleep):
# 	global dict1
# 	dict1[item] = listsleep
# 	return dict1

# def prin(dict1, word):
# 	# val = dict1.value()
# 	# list2 = []
# 	# print('hello')
# 	# print(dict1[word])
# 	dict2 = {}
# 	for each in dict1[word]:
# 		items = each.split(",")
# 		# print(items)
# 		list1 = []
# 		if items[1] not in dict2:
# 			list2 = []
# 			list1.append(items[0])
# 			list1.append(items[2])
# 			list1.append(word)
# 			list2.append(list1)
# 			dict2[items[1]] = list2
# 		else:
# 			# print("hello")
# 			list1.append(items[0])
# 			list1.append(items[2])
# 			list1.append(word)
# 			list2.append(list1)
# 			# dict2[items[1]] = list2
# 	fooddict = dict2
# 	timelist = []
# 	for each in fooddict:
# 		if each not in timelist:
# 			timelist.append(each)
# 	# print(timelist)
# 	if len(timelist)>1:
# 		if timelist[0]>timelist[1]:
# 			print(word + ":")
# 			print(timelist[0] + ":")
# 			for each in fooddict[timelist[0]]:
# 				print("- "+each[1] + ": " + each[0])
# 			print(timelist[1] + ":")
# 			for each in fooddict[timelist[1]]:
# 				print("- "+each[1] + ": " + each[0])
# 		else:
# 			print(word + ":")
# 			print(timelist[1] + ":")
# 			for each in fooddict[timelist[1]]:
# 				print("- "+each[1] + ": " + each[0])
# 			print(timelist[0] + ":")
# 			for each in fooddict[timelist[0]]:
# 				print("- "+each[1] + ": " + each[0])
# 	else:
# 			print(word + ":")
# 			print(timelist[0] + ":")
# 			for each in fooddict[timelist[0]]:
# 				print("- "+each[1] + ": " + each[0])


# def priin(dict1):
# 	# print(dict1)
# 	pass


# if __name__ == '__main__':
# 	main()
# # def FoodLog(data):
# # 	# print(data[1:])
# # 	# food = {}
# # 	# res = {}
# # 	data = data[1:]
# # 	str1 = ''.join(data)
# # 	str1 = str1.split(",")
# # 	# print(str1[0])
# # 	if str1[0] not in food:
# # 		food[str1[0]] = str1[1:]
# # 		res['Food'] = food
# # 	print("Food:")
# # 	for key,val in res.items():
# # 		for key1,val1 in val.items():
# # 			print(val1[0])
# # 			# print(key1,val1)
# # 			print("- " + val1[1] + ": " + key1)
# # 	# display(res)

# # def display(res):
# # 	# 	for key,val in res.items():
# # 	# 	for key1,val1 in val.items():
# # 	# 		if val1[0] not in result:
# # 	# 			result[val1[0]] = val1[1]
# # 	# 			# print(val1[0])
# # 	# 		else:
# # 	# 			result[val1[0]] += val1[1]

# # 	# 		# print(key1,val1)
# # 	# 			print("- " + val1[1] + ": " + key1)
# # 	# print(result)

# # 	# result = {}
# # 	# str1 = ""
# # 	# time = ""
# # 	# for key,val in res.items():
# # 	# 	for key1,val1 in val.items():
# # 	# 		time = val1[0]
# # 	# 		# print(val1[0])
# # 	# 		str1 = "- " + val1[1] + ": " + key1
# # 	# 		result.update({time:str1})
# # 	# 		# print(key1,val1)
# # 	# 		# print("- " + val1[1] + ": " + key1)
# # 	# print(result)
# # 	for key,val in res.items():
# # 		for key1,val1 in val.items():
# # 			print(val1[0])
# # 			# print(key1,val1)
# # 			print("- " + val1[1] + ": " + key1)


# # def WaterLog(data):
# # 	data = data[1:]
# # 	str1 = ''.join(data)
# # 	str1 = str1.split(",")
# # 	# print(str1[0])
# # 	water = {}
# # 	water_res = {}
# # 	if str1[0] not in water:
# # 		water[str1[0]] = str1[1:]
# # 		water_res['Water'] = water
# # 	# print("Water:")
# # 	print("Water:")
# # 	display(water_res)
# # 	# print(water_res)

# # def WeightLog(data):
# # 	data = data[1:]
# # 	str1 = ''.join(data)
# # 	str1 = str1.split(",")
# # 	# print(str1[0])
# # 	weight = {}
# # 	weight_res = {}
# # 	if str1[0] not in weight:
# # 		weight[str1[0]] = str1[1:]
# # 		weight_res['Weight'] = weight
	
# # 	print("Weight:")
# # 	display(weight_res)

# # def PhysicalLog(data):
# # 	data = data[1:]
# # 	str1 = ''.join(data)
# # 	str1 = str1.split(",")
# # 	# print(str1[0])
# # 	physical = {}
# # 	phy_res = {}
# # 	if str1[0] not in physical:
# # 		physical[str1[0]] = str1[1:]
# # 		phy_res['PhysicalActivity'] = physical
# # 	print("PhysicalActivity:")
# # 	display(phy_res)

# # def SleepLog(data):
# # 	data = data[1:]
# # 	str1 = ''.join(data)
# # 	str1 = str1.split(",")
# # 	# print(str1[0])
# # 	sleep = {}
# # 	sleep_res = {}
# # 	if str1[0] not in sleep:
# # 		sleep[str1[0]] = str1[1:]
# # 		sleep_res['Sleep'] = sleep
# # 	# print("Water:")
# # 	print("Sleep:")
# # 	display(sleep_res)

# # def main():
# # 	lines = int(input())
# # 	global food
# # 	global res
# # 	food = {}
# # 	res = {}
# # 	for x in range(lines):
# # 		data = input().split(" ")
# # 		if data[0] == "Food":
# # 			FoodLog(data)
# # 		# if data[0] == "Water":
# # 		# 	WaterLog(data)
# # 		# if data[0] == "PhysicalActivity":
# # 		# 	PhysicalLog(data)
# # 		# if data[0] == "Weight":
# # 		# 	WeightLog(data)
# # 		# if data[0] == "Sleep":
# # 		# 	SleepLog(data)
# # 		# if data[0] == "Summary":
# # 		# 	print("Summary")
# # 		# 	# FoodLog(data)
# # 			# print(WaterLog(data))
# # 			# print(PhysicalLog(data))
# # 			# print(WeightLog(data))
# # 			# print(SleepLog(data))

# # if __name__ == '__main__':
# # 	main()