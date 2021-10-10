#Programed by Everin-k
#make a dictionaray which takes input and gives a output of that input meaning.
dictionary = {}
print ("This is your own dictionary where you can add pairs of words")
options = {'help':'to get help', 'find':'to find anything into your dictionary', 'add':'to add anything into dictionary', '      ':'to get the list of pairs'}
print (options)
while 1:
    uinput = input()
    if uinput == 'help':
        print ("*************Not defined***************")
    elif uinput == 'find':
        key = input("Type the keyword here: ")
        print (dictionary.get(key))
    elif uinput == 'add':
        word = input("Enter the word: ")
        meaning = input("Enter the meaning: ")
        dictionary.update({word:meaning})
        print ("Succesfully added pair in the dictionary")
    else:
        print (dictionary.items())