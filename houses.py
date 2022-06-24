# Jack's House Problem

# Came across this problem in an OA. Language was a little confusing so it took me a while to figure out the nature of the problem 
# and in the end I was only able to write a solution that solved one of the base cases by working backwards.
# Afterwards, I tried to solve it again on my own and drawing out the input really helped me understand the problem.
# I've come up with a solution that *should* pass all of the tests. (I dont remember the test cases or the input restrictions)
# Complexity is O(n); two for loops that iterate once n-times = O(n+n) = O(n) 

# DESCRIPTION: 
# Jack wants to build a house on the biggest piece of land possible between two houses on the street. We're going to help him 
# figure out where those houses are. All of the houses are in a straight line with house numbers 1 to N, and house position as distance 
# from the origin / street entry.
#
# INPUT:
# int 'N', for the number of houses on the street.
# list 'houses', containing inner lists of length 2 containing house number, and house position from the starting point.
#
# TASK:
# Find the largest piece of land between any two adjacent houses. In the event of a tie, return the houses closest to the origin.

import random

def findHouses(houses):

    # Initialize empty dictionary to hold house number and house position pairs.
    numbersAndPositions = {}
    
    # Store the number/position pairs in a hash map
    for index in range(len(houses)):
        # { key=HOUSE_NUMBER : value=HOUSE_POSITION }
        numbersAndPositions[houses[index][0]] = houses[index][1]
    
    # variable to hold largest distance between houses
    maximum_Distance = 0

    # Calculate the distance between adjacent houses, assuming the house numbers start at 1 and increment by one.
    for index in range(1, len(houses)):
        distanceBetweenHouses = abs(numbersAndPositions[index] - numbersAndPositions[index+1])
        if distanceBetweenHouses > maximum_Distance:
            firstHouse = index
            secondHouse = index+1
            maximum_Distance = distanceBetweenHouses
    
    # Return an ascending list of the two houses with the largest area of land between them.
    return [firstHouse, secondHouse]


if __name__ == "__main__":
    
    # Set up the scenario. Make N houses and give them random positions (in ascending order?)
    N = input("How many houses are on the street?")
    houses = []
    
    # Create houses
    for number in range(1, int(N)+1):
        houses.append([number])
    
    # Create positions and order them
    position = random.sample(range(0, 100), int(N))
    position.sort()

    # Assign positions to the houses
    for index in range(int(N)):
        houses[index].append(position[index])
    
    # Print the input so we can validate it later.
    print("Input N: " + str(N))
    print("House number and position list: " + str(houses))
    print("Solution : " + str(findHouses(houses)))
