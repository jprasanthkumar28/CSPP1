# To give the frequency of every digit in given array.
# arr = [2,2,2,3,1,5,1,3]
arr = input().split()
# print(arr)

dup = set(arr)
res = {}
# print(dup)
for i in dup:
	res = arr.count(i);
	print(i , ":" , res)