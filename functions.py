

#from square_func import square #to only input a function from that file
import square_func

#to create a function
def cube(x):
    return x * x * x

for i in range(6):

    #print(f"the square of {i} is {square(i)}")
    print(f"the square of {i} is {square_func.square(i)}", end=" ")
    print(f"and the cube of {i} is {cube(i)}")

square_func.thankyou()

