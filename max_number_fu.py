def function ():
    i=0
    while i<len(number):
        j=0
        num=0
        while j<len(number[i]):
            if number[i][j]>num:
                num=number[i][j]
            j+=1
        i+=1
        print(num)
number=[[45,21,42,63],[12,42,42,53],[42,90,78,13,65],[67,89,45,73,78]]
function()