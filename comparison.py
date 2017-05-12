""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    open_file = open(filename)
    read_file = open_file.read()
    list_lines = read_file.split("\n")
    list_lines.pop()
    return list_lines



def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """

    # Write your code below.
    file_1_open = open(lst1)
    file_1_read = file_1_open.read()
    file_1_list = file_1_read.split("\n")
    file_2_open = open(lst2)
    file_2_read = file_2_open.read()
    file_2_list = file_2_read.split("\n")
    fruits_in_common = []
    for fruit in file_1_list:
        if fruit in file_2_list:
            fruits_in_common.append(fruit)

    return fruits_in_common


# Call your functions at the bottom, after they've been defined.
#open_and_read_file(raw_input("File name: "))
compare("fruits_1.txt", "fruits_2.txt")
print compare("fruits_1.txt", "fruits_2.txt")