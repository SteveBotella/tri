# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def tri():
    int_list = [13, 15, 12, 17, 15, 30, 17, 28, 30, 28]
    string_list = ["Fifi", "Riri", "Loulou", "Zoubi", "Zouba"]
    list_length = len(int_list) + len(string_list)
    result_list = []
    i = 0

    while i < list_length:
        if i < len(int_list):
            result_list.append(int_list[i])
        if i < len(string_list):
            result_list.append(string_list[i])
        i += 1
    return result_list


def main():
    print(tri())


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
