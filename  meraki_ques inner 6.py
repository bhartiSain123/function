def driver(speed):
    speeds=speed-70
    point=speeds//5
    if speed<=70:
        print("ok")
    elif speed>70:
        print("point",point)
    elif point>12:
        print("licence suspended")
s=int(input("enter a speed"))
driver(s)
