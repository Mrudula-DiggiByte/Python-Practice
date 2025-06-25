age = 14
if(age>=18):
    print("can vote and apply for license")
    print("can drive")
else:
    print("cannot vote")   

light ="pink"
if(light =="red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")         


num=5

if(num>2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")    


#grading system
marks = int(input("enter the marks"))
if(marks >= 90):
    print("grade = A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
else:
    print("grade D")            


age = 1
if(age >= 18):
    if(age >=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# 
# 
# WAP to check if a number entered by the user is odd or even
num=int(input("Enter the number"))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")      
# 
#WAP to find the greatest of 3 numbers entered by the user
a=int(input("Enter num1"))
b=int(input("Enter num2"))
c=int(input("Enter num3"))   

if(a>b and a>c):
    print("A is greater")
elif(b>a and b>c):
    print("B is greater")
else:
    print("C is greater")        

#WAP to check if a number is a multiple of 7 or not
n=int(input("Enter the num"))
if(n%7==0):
    print("Multiple")
else:
    print("Not a multiple")    