def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return"Error: Division by zero"
    return x/y

n1 = float(input("Enter first number => "))
n2 = float(input("Enter second number => "))

op = input("Enter your choice +,-,/,* => ")
print("<<< Simple Calculator >>>")
print("Choose Operation:")
print("1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)")

if op=='+':
    result=add(n1,n2)
elif op=='-':
    result=subtract(n1,n2)
elif op=='*':
    result=multiply(n1,n2)
elif op=='/':
    result=divide(n1,n2)
else:
    result="Invalid Operator"

print("Result:",result)