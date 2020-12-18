#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program asks you to input a list of numbers  it it will reverse it


def main():
    number = print(" I am  going to reverse inputed number")
    number_string = input('Enter a number : ')
    reversed = 0

    # process & output
    try:
        number = int(number_string)

        while (number != 0):
            reverse = int(number % 10)
            reversed = reversed*10 + reverse
            number = int(number/10)
        print(reversed)
    except ValueError:
        print('Given input is not a number.')


if __name__ == "__main__":
    main()
