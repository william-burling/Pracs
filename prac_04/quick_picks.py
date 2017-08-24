import random

NUMBERS_PER_LINE = 5
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_picks = int(input("How many picks? "))
    while number_of_picks < 0:
        print("That makes no sense!")
        number_of_picks = int(input("How many picks? "))

    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
