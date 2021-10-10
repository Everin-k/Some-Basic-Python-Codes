#Program by Everin-k
#A pyhton bot which takes commmands and gives output related to that command.
dictionary = {"hey":"Hello","hello":"hey"}
print ("This is a python bot which can reply you according to your command;")
options = {'help':'to get help', '      ':'to get the list of pairs'}
print (options)
while 1:
    command = input("Enter the command here:\n")
    if command == 'help':
        print ("*************Not defined***************")
    elif command == dictionary:
        print (dictionary.get(command))
    else:
        print (dictionary.items())