# Print 1st num and sum of middle nums and last num
#    i/p : 123459
#   o/p: 1149

s = "12345679520"
print("Given number is ---> ", s)
sumOfNum = 0
for i in range(0,len(s),1):
  middle = s[i+1:len(s)-1]
  # print(middle)
  for i in middle:
    sumOfNum += int(i)
    break
result = s[0] + str(sumOfNum) + s[len(s) - 1]
print(result) 