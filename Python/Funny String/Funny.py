# def main():
#   inp = int(input())
#   for _ in range(inp):
#       text = input()
#       funny(text)
# def funny(text):
#   rever = text[::-1]
#   count = 0;
#   for i in range(1,len(text)):
#       te = abs(ord(text[i]) - ord(text[i-1]))
#       re = abs(ord(rever[i]) - ord(rever[i-1]))
#       if te == re:
#           count += 1;
#   if count == len(text) - 1:
#       print("Funny")
#   else:
#       print("Not Funny")
# main()
# 
def funnyString(s):
    # Complete this function
    rev = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(rev[i+1]) - ord(rev[i])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        print(funnyString(s))
