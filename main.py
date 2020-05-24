#changelog v 0.1
    #updated from 3-1 to 1 - 1
    #added spaces!
    #fixed bug about not random, did not evern exncrypt LOL
    #added innport key
    #fixed decoder pogu xqcL
import random
random.seed()
#password is decrypted text
def checkempy():
    for i in y:
        if i == "":
            return True
    return False

def intcheck():
    for i in y:
        for e in prob:
            if i == e:
                return True
            else:
                continue
    return False
def where(thing):
    for i in y:
        if i == thing:
            return y.index(i)
def exists(operand):
    for i in y:
        if i == operand:
            return True
    return False

random.seed()
y = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
q = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
counter = 0
prob = list("|:;?/>.<,+=_-!@#$%^&*()~}{`")
#the encrypt list gen
while checkempy():
    pos = random.randint(0, 26)
    if y[pos] == "":
        for i in prob:
            if not exists(i):
                y[pos] = i
                q[pos] = i
    #print(y)
#import key
c = list(input("Key: "))
if "`" in c:
    q = c
    y = c

#print (y)
#aplhabet LOL
x = list("abcdefghijklmnopqrstuvwxyz ")
#replace all numbs with letters
while intcheck():
     for i in y:
         y[y.index(i)] = x[y.index(i)]
     #print ("yp")

#print (y)
e = "".join(q)
#makesurepw is viable
password = "."
def works():
    forb = list("<,>.?:;{[}]|/+=_-)(*&^%$#@!~`1234567890'\"\\")
    for i in password:
        for e in forb:
            if i == e:
                return False
    return True
#password switcher
while not works():
    password = list(input("Word: "))

for i in password:
    password[password.index(i)] = str(y.index(i))

#print (password)
#password to symbol
for i in password:
    password[password.index(i)] = str(q[int(i)])

#print(password)

#combiner
pasd = "".join(password)
print ("this is the encrypted text: " + pasd)

#password compileer
print("The key is: " + e)
