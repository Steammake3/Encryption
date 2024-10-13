import random
import hashlib as nsa

print("\n")

cs = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,. -+=*/?!()"
xtra = "<>1234567890[]'\""
f = open("ede.txt", "r"); txt = f.read(); f.close()
k = int(input("Key? "))

w = nsa.sha256((f"{k}"*k).encode()) #custom hash for each numerical value
w = w.hexdigest() #Get digest
w = w[(k*27)%64:(k*27+9)%64] #find the digits
w = int(w, 16) #convert hex text to decimal integer

t = f"A-{k} is an encryption technique"
for d in range(int(w*0.12-k*1.74+3)%10000000):
    t = nsa.sha256(t.encode()).hexdigest()

random.seed(int(t[(k*217)%64:(k*217+20)%64], 16)%7248901)

xor = lambda t, c: ''.join(c[c.find(s)^random.randint(0,len(c)-1)] if s in c else (xtra[xtra.find(s)^random.randint(0, len(xtra)-1)] if s in xtra else s) for s in t)

print(xor(txt, cs))