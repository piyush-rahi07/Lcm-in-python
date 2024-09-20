a = int(input("enter the number : \n"))
b = int(input("enter the number : \n"))

maxnum = max(a,b)

while(True):
    if(maxnum%a==0 and maxnum%b==0):
        break
    maxnum=maxnum+1

print(f"the LCM of {a} and {b} is {maxnum}")