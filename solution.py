userInput=int(input("Enter number to see the reverse: "))

# reverse=0
reverse=""
temp=userInput

while(temp > 0):
    rest=temp%10
    # if a number ends with a 0, then this will not work
    # reverse=(reverse*10)+rest 
    reverse=reverse+str(rest)
    temp=(temp-(rest))//10

print("reverse", str(reverse))
