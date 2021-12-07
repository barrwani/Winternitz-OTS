import hashlib,random,sys, binascii
hexdigest_size=16
a = 1*10**32
b = 9.99999999999999999999999999999999*10**32
x=random.randint(a,b)
print("Key X (private) is:", x)

y = bin(x)
for i in range(3):
    y = hashlib.sha512(y.encode()).hexdigest()

print ("Key Y (public) is:", y)

