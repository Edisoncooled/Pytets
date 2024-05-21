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
            if letters.index(i)+s > len(letters):
                res+=letters[letters.index(i)+s - len(letters)]
            else:
                res+=letters[letters.index(i)+s]
        return(res)
    else:
        for i in t:
            if letters.index(i) < s:
                res+=letters[len(letters) - (s - letters.index(i))]
            else:
                res+=letters[letters.index(i)-s]
        return(res)
       
    
        
print(cesar(direction, text, int(shift)))

