from math import sqrt #call operator from library


def pythagorean_pair(a,b):
    c =sqrt((a**2)+(b**2)) #pythagorean theorem
    c_int = int(c) #collect the hypotenuse value as an int
    test_pythagorean_pair = ((c_int-c) == 0)#identifies if its acc a pythagorean pair or not 
    return test_pythagorean_pair #allow true or fasle to be returned
    


print(pythagorean_pair(int(input("enter another real value: ")), int(input("enter another real value: ")))) #calling the function on the user input

    


    
