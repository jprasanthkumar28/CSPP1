#define the gen_primes function here
def is_Prime(n):
	for index in range(2, n):
		if n % index == 0:
			return False
	return True
#genrate gen Primes		
def genPrimes():
    value = 2
    while True:
    	if is_Prime(value):
    		yield value
    	value += 1

def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print (p)
	
if __name__== "__main__":
	main()
