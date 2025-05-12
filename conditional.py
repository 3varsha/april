"""
this is python pgm
I added 1 stmt
"""
#Above 59 age people will get pension scheme using this cond. write a if-else pgm
age=int(input("enter number : "))
if age>=59:
    print("people will get pension")
else:
    print("not eligible for pension")    



#pgm using if-elif-else statement
#1)pgm
score=int(input("Enter score"))
if score>=70:
    print(f"score is {score} then distinction")
elif score>=50:
    print(f"score is {score} then pass")
elif score>=40:
    print("average")
else:
    print("fail")    


#2)pgm
name=input("enter name")
if name=="vars":
    print("var")
elif name=="sri":
    print("sris")
else:
    print("invalid")

    

#Using short-hand if else check given number is even or odd
n1=int(input("Enter number : "))
print("number is even" if n1%2==0 else "number is odd")



#simple calculator pgm  that takes 2 numbers & operators(+,-,*,/)as i/p & perform the operations & display o/p
n1=int(input("enter n1 : "))
n2=int(input("enter n2 : "))
operator=input("enter operator(+,-,*,/):")
if operator=="+":
    print(n1+n2)
elif operator=="-":
    print(n1-n2)
elif operator=="*":
    print(n1*n2)
elif operator=="/":
    print(n1/n2)
else:
    print('invalid')




#take 3 no.'s & write a python pgm to find the largest among these 3 no.'s
n1=int(input("Enter number1 :"))
n2=int(input("Enter number2 :"))
n3=int(input("Enter number3 :"))
if n1>=n2 and n1>=n3:
    largest=n1
elif n2>=n3 and n2>=n1:
    largest=n2
else:
    largest=n3
print("largest number",largest)
