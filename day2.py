import random
def awesome():
 print ("Cool! See you tomorrow")

def okay ():
 print ("Okay, I'll see you tomorrow")

def horrible ():
 print ("That's too bad... hope tomorrow is better")


def ask ():
    q=["How was your day?  ", "How was your coffee?  ", "How was your date?  "]
    return q[random.randint(0,2)]

for i in range(10):
    x = raw_input(ask())
    print (x)
    if x == 'okay' or x == 'fine':
        okay()
    elif x == 'awesome' or x == 'good' or x == 'great':
        awesome()
    elif x =='horrible' or x == 'bad' or x == 'pretty bad':
        horrible()
    else:
        print ("Yeah, same here... well, I'm off to Starbucks")







