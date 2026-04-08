try:
    print ("1 - Length \n 2 - Temperature")
    choise = int(input("enter your choice 1 or 2: "))

#code for length
    if choise == 1:
        print("length")
        length = float(input("enter your length in meter: "))
        print("1 - Kilometer \n 2 - Feet")
        length_choise = int(input("enter your choise :"))
        if length_choise == 1:
            print(f"{length / 1000} kilometer")
        elif length_choise == 2:
            print(f"{length*3.28084} Feet")    
    
#code for tempreature
    elif choise == 2:
        print("temprature")
        temp = float(input("enter your temprature in celcius:"))
        print(f"{(temp*9/5)+32} Farenhite")
    
    else:
        print('Invalid choice')
    
except:
    ("please try again")