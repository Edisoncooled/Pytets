import string
import random

let_num=input('How many letters?')
num_num=input('How many numbers?')
simb_num=input('How many simbols?')

# All letters
let = list(string.ascii_letters)

# All numbers
num = list(string.digits)

# All symbols
simb = list(string.punctuation)

pass_val = [let, num, simb]

password=[]

password_1=''

for i in range(int.let_num):
    password.append(random.choice(let))

for j in range(int.num_num):
    password.append(random.choice(num))

for k in range(int.simb_num):
    password.append(random.choice(simb))

random.shuffle(password)

for i in password:
    password_1+=i

print(password_1)



