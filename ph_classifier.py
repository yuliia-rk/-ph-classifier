print ('Please, write "done" to finish')
while True:
    pH = input('Type pH here: ')
    if pH == 'done':
        print ('Have a nice day!')
        break
    try:
        pH = float (pH)
        if 0 < pH < 7:
            print ('This is an acid.')
        elif pH == 7:
            print ('This is neutral compound.')
        elif  7 < pH < 14:
            print ('This is a base.')
        else:
            print ('Invalid input, pleas try again')
        continue
    except: 
        print ('Please, write only numbers here')