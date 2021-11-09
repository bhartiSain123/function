def function():
    i=0
    lower=0
    upper=0
    while i<len(s):
        if s[i]>="a" and s[i]<="z":
            lower+=1
        elif s[i]>="A" and s[i]<="Z":
            upper+=1
        i+=1
    print("lower case",lower)
    print("upper case",upper)
s="The quick Brow fox"
function()
