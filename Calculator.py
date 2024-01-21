# Write a program to make a calculator that does all arithemetic, logical and comparision operations.

#Arithemetic Operators

num1=input('Enter the first variable\n')
num2=input('Enter the second variable\n')
a=float(num1)
b=float(num2)
c=a+b
d=a-b
e=a*b
f=a%b
g=a/b
h=a//b
print("The results for arithematic Operations are:\n")
print("Sum=",c)
print("Difference=",d)
print("Product=",e)
print("Modulus=",f)
print("Quotient=",g)
print("Float Division=",h)

#Comparision Operators

print("a<b",a<b)
print("a>b",a>b)
print("a==b",a==b)
print("a!=b",a!=b)
print("a>=b",a>=b)
print("a<=b",a<=b)

#Logical Operators

print("all logical operations are ")
a1 = True
b1 = False
print(a1 and b1) 
print(a1 or b1)
print(not a1)