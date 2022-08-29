#1. Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c  
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
x=int(input("Enter value of x : "))
soln= lambda a,b,c,x : ((a*x)*(a*x))+(b*x)+c
print(soln(a,b,c,x))