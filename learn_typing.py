from sys import argv

script, base = argv

txt = open(base, 'r')

text = txt.read()

print "This is a programm to train typing"
print 'At first you will see the whole text, then you will see a single word, type it in exactly as you see it, then press Enter \n And don\'t forget to have fun!'

raw_input('press \'any key\' to continue, if you can\'t find \'any key\', just press Enter')

print text

raw_input('press \'any key\' to continue, if you can\'t find \'any key\', just press Enter')

string = text.replace('\n', ' ')

words = string.split(''' ''')

# print words

words.append('The End')

def practice():
    print words[0]
    typed = raw_input('> ')
    current_word = words[0]
    if current_word == 'The End':
        print 'Great! You\'re done!'
        exit()

    elif current_word == typed:
        words.pop(0)
        practice()
    # The next two are cheats!
    elif typed == 'Yog_Sothoth':
        print '''Great! You're done! Praise Yog Sothoth!'''
        exit()
    elif typed == 'd':
        words.pop(0)
        words.pop(0)
        practice()
    else:
        print 'Wrong, try again!'
        practice()

practice()


