# Packet creator:
def encoding2bin(num):
    num = str(num)
    if num.find(".") > 0:
        whl, dec = num.split(".")
        whl = int(whl)
        dec = int(dec)
    else:
        whl = num
        whl = int(whl)
        dec = 0
        
    whlb = bin(whl)
    decb = bin(dec)
    
    return whlb, decb

def decoding2float(whlb,decb):
    whl = int(whlb, 2)
    dec = int(decb, 2)
    num = str(whl)+"."+str(dec)
    num = float(num)
    
    return num


