vowelCount=0
value = input("Enter a string  ")
for char in value:
	if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
		vowelCount += 1
print(vowelCount)
