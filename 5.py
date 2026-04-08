low = int(input("Enter lower range : "))
up = int (input("Enter upper range : "))
for n in range (low, up + 1) :
    if n > 1 :
        for i in range (2, n) :
            if (n % i) == 0 :
                break
else :
   print (n)
#Output :
#Enter lower range : 10