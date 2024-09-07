import math
#chars = "~!@#$%^&*()_+`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?\\ "

#x = "p"

#def stuff(inp, s, a):
    #return (chars.find(inp)/len(chars))*s + a
def xor(a, b):
    return bool(int(a)) != bool(int(b))

def txt2bin(s):
    out = []
    for char in s:
        binary = f'{ord(char):b}'
        binary = (8-len(binary))*"0" + binary
        out.append(binary)
    return out

def key(k : float, v : float):
    """Psuedo random bit generator (deterministic)
    k : the key, v : the position of the bit"""
    return 1 - math.floor((k * math.pow(v, 5.2)) % 2)

x=" "
#txt2bin=lambda s : [(8-len(bin(ord(w))[2:-1]))*"0"+bin(ord(w))[2:-1] for w in s]
unplain = txt2bin(x)
# TODO: XOR for each bit with true key
for i in range(1, len(unplain)*8+1):
    t = unplain[i // 8]
    index = i % 8


print(txt2bin(x))