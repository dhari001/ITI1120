#a)

def sidereal_seconds(sidereal):
    seconds = (sidereal*365.26)*86400.0 #convert years into seconds
    print("The number of seconds is", seconds)


numOfSidereal = float(input("Enter number of sidereal years: ")) #userinput
sec = sidereal_seconds(numOfSidereal)#calling function on user input to convert



#b)
def lightseconds_km(light_seconds):
    kilometers = light_seconds*300000.0 #convert seconds into distance
    print("The distance is",kilometers,"km") 

numOfLightseconds = numOfSidereal*365.26*86400.0 #years converted into seconds from part a
kiloM = lightseconds_km(numOfLightseconds) #calling function on seconds variable to convert into distance

#c)

star_1 = float(input("Enter the distance to the first star: ")) #userinput
star_2 = float(input("Enter the distance to the second star: ")) #userinput

def sidereal_seconds(sidereal):
    seconds = (sidereal*365.26)*86400.0 #convert years into seconds
    

 
numOfSidereal = star_1 + star_2 #total distance in lightyears
sec = sidereal_seconds(numOfSidereal) #convert lightyears into seconds


def lightseconds_km(light_seconds):
    kilometers = light_seconds*300000.0 #convert seconds into distance
    print("The distance between the two stars is",kilometers, "km")

numOfLightseconds = numOfSidereal*365.26*86400.0 #years converted into seconds from initial input in part c
kiloM = lightseconds_km(numOfLightseconds) #calling function on seconds variable to convert into distance
