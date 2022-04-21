#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 04/21/2022
# Description: Gets a number from user, calculates the power of every number
# within the range of 0 to the entered number
def main():
    num = input("Enter a positive number to be squared: ")
    # Catching any invalid input
    try:
        number = int(num)
        # Ensures number is positive
        if number >= 0:
            # For loop for going through each number to calculate the square
            for counter in range(0, number + 1):
                square = counter * counter
                # Displaying results
                print("The square of {0} is {1}".format(counter, square))
        else:
            print(
                "The inputted number must be greater than or equal to 0 for this program"
            )
    except ValueError:
        print("Invalid Input")


if __name__ == "__main__":
    main()
