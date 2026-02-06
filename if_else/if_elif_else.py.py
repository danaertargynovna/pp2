#1 example
a=input()
x=7
if(len(a)>x):
    print("string len greater than x")
elif(len(a)==x):
    print("equal")
else:
    print("x is greater")

#2 example 
x=int(input("num1"))
y=int(input("num2"))
if(x>y):
    print("x greater")
elif(x==y):
    print("equal")
else:
    print("y greater")

#3 example

pp_grade=int(input())

if(pp_grade>70):
    print('ura stependia')
elif(50<pp_grade<70):
    print("bez stependii")
else:
    print("retake")
#4 example
x=4
if(x>0):
    print("x is positive")
elif(x<0):
    print("xis negative")
else:
    print("x is 0")

#5 example

a=100
b=50
if(a+b>100):
    print("Good")
elif(a+b<100):
    print("Bad")
else:
    print("Okay")