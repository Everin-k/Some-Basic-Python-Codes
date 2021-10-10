###Guess the number**
try:
    import random
    choice = random.randint(1, 100)
    n =choice
    print ("Welcome to Guess the number")
    print ("Guess a number between 1 to 100, but you hava a limit of 10 times so, be carefull\n")
    gnum = 1
    while (gnum <=10):
        gn = int(input("Guess the number:- \n"))
        if gn <int(choice):
            print ("you entered lesser number please enter a greater number. \n")
        elif gn>int(choice):
            print ("you entered greater number please enter a smaller number. \n")
        else:
            print ("You won \n")
            print (gnum, "number of guess you took to finish. ")
            break
        print (10-gnum, "number of guesse left")
        gnum = gnum+1
    if (gnum>10):
	    print ("game over")
	    print (f"Computer's choice:-{choice}")
except ValueError:
    print (f"Try to enter a 'Integer' not a string or floating point number. ")