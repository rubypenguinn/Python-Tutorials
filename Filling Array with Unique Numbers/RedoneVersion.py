# This is the better method
import random
import sys


def create_unique_list(list_size, number_range):
    unique_list = []
    while len(unique_list) < list_size:
        temp_num = random.randrange(0, len(number_range))
        unique_list.append(number_range[temp_num])
        number_range.remove(number_range[temp_num])
    validate_uniqueness(unique_list)
    return unique_list


def validate_uniqueness(unique_list):
    print(unique_list)
    dict_ = {}
    for i in unique_list:
        if i in dict_:
            print("Your algorithm sucks", file=sys.stderr)
            exit()
        dict_[i] = i
    print("Your algorithm is somewhat competent, for now.")


# main method
if __name__ == '__main__':
    num_of_indexes = 10  # list size
    number_range = 50  # range of random numbers to choose from

    if number_range < num_of_indexes:
        print("Make sure you have a large enough range.")
        exit()

    temp_list = [x for x in range(number_range)]
    create_unique_list(num_of_indexes, temp_list)
