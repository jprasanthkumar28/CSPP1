# Write a program to print 0 if the ascii code of a character is even and 1 if the ascii code of the character is odd in a given string.
# Input : abcD
# Output : 1010
s = "AbcfszgdhbjhiskjfhlchgvsglachasiascbkgavkjgkjbD"
for char in s:
  	if (ord(char)) % 2 == 0:
  		print(0,"---",char)
  	else:
  		print(1,"---",char)