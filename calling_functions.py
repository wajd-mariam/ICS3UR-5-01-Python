# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program calls different functions when it's called.


def FahrenheitConverter():
    # input
    celsius = int(input("Enter degrees in C, it will give it back in F: "))

    # process
    Fahrenheit = (celsius * 1.8) + 32

    # output
    print("{} C is {} F.".format(celsius, round(Fahrenheit, 2)))
    print("Thank you for using my program")


def main():
    # call functions
    FahrenheitConverter()


if __name__ == "__main__":
    main()
