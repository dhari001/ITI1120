#xs and ys are coordinates of bottom left corner of a square
#side is length of the line portruding from the coordinates

def in_out(xs,ys,side):
    x_coordinate = float(input("Enter a number for the x-coordinate of a query point: ")) #userinput
    y_coordinate = float(input("Enter a number for the y-coordinate of a query point: ")) #userinput
    boundary = (x_coordinate <= side) and (y_coordinate <= side) #comparing coordinates to actual area
    return boundary #return boolean 



print(in_out(float(input("Enter a value for the starting x-coordinate: ")), float(input("Enter a value for the starting y-coordinate: ")), abs(float(input("Enter a positive value for the length of the square: "))))) #call function on userinputs
        
