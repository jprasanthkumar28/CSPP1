import re
listt = input()
listt = re.sub('[^A-Z0-9-,]+','',listt).split(",")
if len(listt) == 0:
	newdata = []
	print(newdata)
elif len(listt) == 1:
	print([listt[0],listt[0]])
else:
	listt = list(map(int,listt))
	for i in range(len(listt)):
	    for j in range(i + 1, len(listt)):
	        if listt[i] > listt[j]:
	           listt[i], listt[j] = listt[j], listt[i]
	print([listt[1], listt[len(listt) - 2]])
# for i in range(len(listt) - 1):
# 	print(listt[i + 1])