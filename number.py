#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program checks if the entered number is the same as the random number

import random


def main():
    # This function checks if there is over than 30 students
    number_random = random.randint(1, 5)  # a number between 1 and 5

    # Input
    number_user = int(input("Enter a number:  "))
    print("")

    # Process & Output
    if number_user == number_random:
        print("You are right! ", number_random)
    else:
        print("You are wrong!")


if __name__ == "__main__":
    main()
