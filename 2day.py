#programed by Everin-k
#console based calculator
def add():
    f1 = int(input("enter the first number:\n"))
    f2 = int(input("enter the second number:\n"))
    print ("sum of these two number is:", f1 + f2)
def sub():
    f1 = int(input("enter the first number:\n"))
    f2 = int(input("enter the second number:\n"))
    print ("difference between these two number is:", f1 - f2)
def mul():
    f1 = int(input("enter the first number:\n"))
    f2 = int(input("enter the second number:\n"))
    print ("product of these two number is:", f1 * f2)
def div():
    f1 = int(input("enter the first number:\n"))
    f2 = int(input("enter the second number:\n"))
    print ("Dividend of these two number is:", f1 / f2)
if __name__=="__main__":
    while 1:
        print ("Welcome to the world of mathematics:...........................")
        operation = input("Enter the operation which you want to do:\n")
        if operation == 'add':
            add()
        elif operation == 'sub':
            sub()
        elif operation == 'mul':
            mul()
        elif operation == 'div':
            div()