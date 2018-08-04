'''*******Palindrome**********
value = input()
str = ""
for i in value:
	str = i + str
if value == str:
	print("Palindrome")
else:
	print("Not Palindrome")'''
'''*********Reverse of String**********
value = input()
str = ""
for i in value:
	str = i + str
print(str)'''
'''**************To print in vertical way*************
value = input()
for i in value:
	print(i)'''
'''value = input()
for i in value:
	str = i + str
print(str)'''
'''*****Vowels and Consonents***********
value = input()
vow =""
cons=""
l = len(value)
for i in range(0,l,1):
	if value[i] in ['a', 'e', 'i', 'o', 'u']:
		vow += value[i]
	else:
		cons += value[i]
print(vow)
print(cons)'''

value =input()
count = len(value)
for i in range(0,count,1):
	if value[i].islower()==1:
		print(value[i].upper(),end="")
	else:
		print(value[i].lower(),end="")