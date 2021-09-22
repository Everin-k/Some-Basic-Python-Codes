#Basic console based calculator programed by Everin-k
def add():
    """This is a function to find the sum of two numbers. It takes two input seperated by a space like this:- 2 2"""
    f1, f2= input("Enter the two numbers:\n").split()
    print ("Sum of these two number is:", int(f1) + int(f2))
def sub():
    """This is a function to find the difference of two numbers. It takes two input seperated by a space like this:- 2 2"""
    f1, f2= input("Enter the two numbers:\n").split()
    print ("Difference between these two number is:", int(f1) - int(f2))
def mul():
    """This is a function to find the product of two numbers. It takes two input seperated by a space like this:- 2 2"""
    f1, f2= input("Enter the two numbers:\n").split()
    print ("Product of these two number is:", int(f1) * int(f2))
def div():
    """This is a function to find the dividend of two numbers. It takes two input seperated by a space like this:- 2 2"""
    f1, f2= input("Enter the two numbers:\n").split()
    print ("Dividend of these two number is:", int(f1) / int(f2))
if __name__=="__main__":
    print ("Welcome to the world of mathematics:...........................")
    while 1:
        operation = input("Enter the operation which you want to do:\n")
        if operation == 'add':
            add()
        elif operation == 'sub':
            sub()
        elif operation == 'mul':
            mul()
        elif operation == 'div':
            div()