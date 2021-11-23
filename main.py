# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def main():
    random_list = random.sample(range(0, 10000), 1000)

    print(random_list)

    random_list.sort()

    print(random_list)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
