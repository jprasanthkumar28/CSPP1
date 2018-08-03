first = input("Enter main string : ")
sub = "bob"
c = 0
j=0
for i in range(len(first)-2):
	if first[i]=='b' and first[i+1]=='o' and first[i+2]=='b':
			c += 1
print(c)