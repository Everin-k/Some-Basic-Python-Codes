#simple and short calculator
print ("Welcome to Simple and short")
def calcu(stri):
    ans = eval(stri)
    return print (ans)
stri = input("Enter here your expression: [num1 operation num2]\n")
calcu(stri)