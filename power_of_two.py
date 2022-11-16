# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 8, 2022
# This program uses a for loop to calculate and /n
# display the “square” (power of 2) starting from 0 until this number./n


def main():
    # set variables
    User_Input = input("Enter a positive integer here: ")
    # check to see if User_input is a string or not
    try:
        User_number = int(User_Input)
        # checks to see if number is lower than 0 then loops to main
        if User_number < 0:
            print("")
            return main()
        # if number is greater than or equal to 0 /n
        # it calculates the power from 0 to that number /n
        elif User_number >= 0:
            for counter in range(User_number + 1):
                power = counter**2
                print()
                print("{}^2 = {}.".format(counter, power))
    except Exception:
        print()
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
