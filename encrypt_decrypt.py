def calc(ch, jump):
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    f=alpha.find(ch)
    if f==-1:
        return ch
    while jump>0:
        if f%2==0:
            f+=67
        f+=1
        f//=2
        f-=1
        jump-=1
    return alpha[f]
def calc2(ch,jump):
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    f=alpha.find(ch)
    if f==-1:
        return ch
    while jump>0:
        f+=1
        f*=2
        f-=1
        jump-=1
        if f>66:
            f%=67
    return alpha[f]
def decode(s):
    res=""
    for i in range(len(s)):
        res+=calc(s[i],i+1)
    return res
def encode(s):
    res=""
    for i in range(len(s)):
        res+=calc2(s[i],i+1)
    return res
def run():
    text =""
    while True:
        j=int(input("1 Encode\n2 Decode\nOther Exit\n"))
        if j>2 or j<1:
            break
        if j==1:
            text=input("Enter text to encode\n")
            print("Encoded: ",encode(text))
        elif j==2:
            text=input("Enter text to decode\n")
            print("Decoded: ",decode(text))
    print("Good Bye")
run()
