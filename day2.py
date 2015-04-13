import random

f = open ('answers.csv', 'w')
savestuff = []

def awesome():
 print ("Cool! See you tomorrow")

def okay ():
 print ("Okay, I'll see you tomorrow")

def horrible ():
 print ("That's too bad... hope tomorrow is better")

def ask ():
    q=["How was your day?  ", "How was your coffee?  ", "How was your date?  "]
    return q[random.randint(0,2)]

while 1 == 1:
    x = raw_input(ask())
    print (x)
    if x == 'okay' or x == 'fine' or x == 'meh' or x == 'nothing special':
        okay()
    elif x == 'awesome' or x == 'good' or x == 'great' or x == 'wonderful' or x == 'amazing' or x == 'really good':
        awesome()
    elif x =='horrible' or x == 'bad' or x == 'pretty bad' or x == 'boring':
        horrible()
    elif x == 'how was yours?':
        print savestuff
        f.write (savestuff.join ("\n"))
        f.write ("")
    else:
        print ("Yeah, same here... well, I'm off to Starbucks")
    savestuff.append(x)

f.close ()









