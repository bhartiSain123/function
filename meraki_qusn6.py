def n(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0:
            sum+=i
        elif i%5==0:
            sum+=i
        i+=1
    print(sum)
h=int(input("enter a number"))
n(h)