def function():
	    pw=input("enter a password")
	    if (pw>="a" and pw<="z" ) or (pw<="A" and pw>="Z") or (pw<="0" and pw>="9") or (pw=="#",pw=="%",pw=="$",pw=="@",pw=="&",pw=="₹"):
	        if len(pw)>=6and len(pw)<=12:
	            print("strong password")
	        else:
	            print("wrong pasword")
	    else:
	        print("wrong paasword")
function()
