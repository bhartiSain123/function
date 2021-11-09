def perfect (n):
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print("perfect numbr")
    else:
        print("not")
a=int(input("enter a number"))
perfect(a)

