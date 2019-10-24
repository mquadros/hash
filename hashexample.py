import hash

password = "MyPassword"

hp1 = hash.hash(password)

print('password1: ' + password)
print('password1: ' + hp1[0])
print('salt: ' + hp1[1])

oldpassword = password
password = "NotMyPassword"

hp2 = hash.hash(password)

print('password2: ' + password)
print('password2: ' + hp2[0])
print('salt: ' + hp2[1])

print('Does ' + password + " match " + oldpassword + "?")
print('match: ' + str(hash.match(hp1[0],hp1[1],password)))


password = "MyPassword"
print('Does ' + password + " match " + oldpassword + "?")

print('match: ' + str(hash.match(hp1[0],hp1[1],password)))