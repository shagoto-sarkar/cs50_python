n = int(input("input a number: "))                             
        #the input is typecasted into int
if n > 0:
    print(f"{n} is a posive number.") #the indentation is important

elif n < 0: #elif is like elseif
    print(f"{n} is a negative number.") 

else:
    print(f"{n} is Zero.")