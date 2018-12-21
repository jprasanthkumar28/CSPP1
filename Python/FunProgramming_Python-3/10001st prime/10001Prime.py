# import sys
# number = int(input().strip())
# for k in range(number):
#     n = int(input().strip())
#     a=[2,3,5,7]
#     i=3
#     j=9
#     while(i<n):
#         flag=0
#         j=j+2
#         for k in range(len(a)):
#             if(a[k]<=int(j**(0.5)) and j%a[k]==0  ):
#                 flag=1    
#                 break     
#         if(flag==0):
#             a=a+[j]
#             i=i+1
#     print(a[n-1])
#     
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
t = int(input().strip())
l=0
i=2
d=[]
for a0 in range(t):
    n = int(input().strip())
    while l<n:
        if(isPrime(i)):
            l+=1
            d.append(i)
        i+=1
    print(d[n-1]) 