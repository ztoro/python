# A programozási tételek visszatérő, egyszerű algoritmusok.

my_numbers = [492, 188, 729, 423, 281, 564, 718, 409, 47, 730, 407, 246, 117, 191, 453, 9, 202, 64, 236, 489, 402, 383,
              745, 2, 905, 634, 965, 720, 803, 285, 752, 872, 969, 576, 709, 650, 445, 805, 485, 737, 519, 836, 584,
              410, 562, 497, 306, 849, 704, 555, 673, 905, 360, 166, 948, 85, 666, 605, 435, 312, 318, 290, 317, 889,
              14, 564, 982, 723, 885, 449, 70, 368, 701, 104, 539, 778, 117, 402, 269, 939, 465, 320, 318, 703, 809,
              254, 749, 71, 880, 523, 223, 846, 218, 868, 728, 939, 176, 471, 240, 143]


# MAXIMUM KIVÁLASZTÁS
def my_max(my_numbers):

    max_number = my_numbers[0]
    for number in my_numbers:
        if number > max_number:
            max_number = number
    return max_number

# MINIMUM KIVÁLASZTÁS
def my_min(my_numbers):

    min_number = my_numbers[0]
    for number in my_numbers:
        if number < min_number:
            min_number = number
    return min_number


# SZÁMLÁLÁS
def my_even(my_numbers):

    even_numbers = 0
    for number in my_numbers:
        if number % 2 == 0:
            even_numbers = even_numbers+1
    return even_numbers

# MÁSOLÁS
def my_even_list(my_numbers):

    even_numbers = []
    for number in my_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# TRY EXCEPT PÉLDA
def my_even_sort(my_numbers):

    even_numbers = []
    for number in my_numbers:
        try:
            print(my_numbers[10])
            if number % 2 == 0:
                even_numbers.append(number)
        except IndexError:
            print("Ups!")
        except KeyError:
            print("keyerror!")
        finally:
            print("end!")
    return even_numbers


print(my_max(my_numbers))
print(my_min(my_numbers))
print(my_even(my_numbers))
print(my_even_list(my_numbers))
print(my_even_sort(my_numbers))
print(my_numbers)