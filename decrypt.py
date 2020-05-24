pahbet = list("abcdefghijklmnopqrstuvwxyz")
def checkifword():
    for i in list(times):
        for e in pahbet:
            if i == e:
                return True
    return False


times = "bruh"
#key = list("@,=/}^~+%{>#.?$&)(!_-<*|:;")
while checkifword():
    times = input("How many words to decrypt? ")
#password = list("!|^,%")
key = list(input("Key: "))
cipher = list("abcdefghijklmnopqrstuvwxyz ")
cipheru = list("|:;?/>.<,+=_-!@#$%^&*()~}{`")
bruh = []
#check if space ava
if times is "":
    times = 1

#importing key
for i in range(int(times)):
    password = list(input("Word: "))
    for i in key:
        bruh.append(int(cipheru.index(i)))
    for i in bruh:
        bruh[bruh.index(i)] = cipher[i]
    #print (bruh)
    for i in password:
        password[password.index(i)] = int(key.index(i))
    #print (password)
    for i in password:
        password[password.index(i)] = cipher[i]
    bruh = []
    goodpw = "".join(password)
    print("text: " + str(goodpw))
