#this script encode or decode input messages

import string

direction=input('write encode if u want encode message, write decode to decode message: ')

text = input('write you message: ')

shift = input('write encode value: ')

def cesar(dir, t, x):
    letters = list(string.ascii_lowercase)

    s = x-(len(letters)*(x//len(letters)))

    res=''

    if dir == 'encode':
        for i in t:
            if i in letters:
                if letters.index(i)+s > len(letters):
                    res+=letters[letters.index(i)+s - len(letters)]
                else:
                    res+=letters[letters.index(i)+s]
            else:
                res+=i
        print(res)
        return rerun()
    else:
        for i in t:
            if i in letters:
                if letters.index(i) < s:
                    res+=letters[len(letters) - (s - letters.index(i))]
                else:
                    res+=letters[letters.index(i)-s]
            else:
                res+=i
        print(res)
        return rerun()

def rerun():
    user = input('write y if u need one more time: ')
    if user == 'y':
        direction=input('write encode if u want encode message, write decode to decode message: ')
        text = input('write you message: ')
        shift = input('write encode value: ')
        cesar(direction, text, int(shift))
    elif user == 'n':
        print('Bye')

cesar(direction, text, int(shift)) 
