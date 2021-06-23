import time
import math

def binary_search_for_num(list_of_numbers, number_to_find):

    def middle_index_of_list(list_of_numbers):
        middle = math.floor((len(list_of_numbers) / 2))
        middle_value = list_of_numbers[middle]
        print(middle_value)
        return middle

    def middle_value_of_list(middle_index, list_of_numbers):
        middle_value = list_of_numbers[middle_index]
        return middle_value

    while middle_value_of_list(middle_index_of_list(list_of_numbers), list_of_numbers ) != number_to_find:
        print(list_of_numbers)

        if middle_value_of_list(middle_index_of_list(list_of_numbers), list_of_numbers ) < number_to_find:
            list_of_numbers = list_of_numbers[middle_index_of_list(list_of_numbers):len(list_of_numbers)]
            print(list_of_numbers)

        else:
            list_of_numbers = list_of_numbers[0:middle_index_of_list(list_of_numbers)]
            print(list_of_numbers)






binary_search_for_num(list(range(0, 100000)), 6589)