# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def main():
    l1 = [13, 15, 12, 17, 15]
    l2 = [12, 13, 20, 17, 14, 18]
    list_length = len(l1) + len(l2)
    result_list = []
    i = 0

    while i < list_length:
        if i < len(l1) and not result_list.count(l1[i]):
            result_list.append(l1[i])

        if i < len(l2) and not result_list.count(l2[i]):
            result_list.append(l2[i])

        i = i + 1

    print(result_list)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
