import sys
from reading_and_writing_matrices import writing_matrix
from reading_and_writing_matrices import show_matrix
from reading_and_writing_matrices_2 import reading_matrix

matrix_B = [
    [-31,29,34],
    [12,11,-25],
    [28,21,-42]
]
matrix_c = [
    [4,41,40],
    [-20,16,-51],
    [38,29,-43]
]


def main():
    dict_matrix = {
        "test2" : matrix_B,
        "test3" : matrix_c
    }
    command = " "
    while command != "quit":
        command_input = input("what is you command?\n")
        parts = command_input.split()
        command = parts[0]
        # This also works
        # running = True
        # while running:
        if command == "read":
            filename = parts[1]
            matrix_name = parts[2]
            matrix = reading_matrix(filename)
            dict_matrix[matrix_name] = matrix
            print ("The file: %s is processed with the key %s"%(filename,matrix_name))
        elif command == "write":
            filename = parts[2]
            matrix_name = parts[1]
            matrix = dict_matrix[matrix_name]
            writing_matrix(filename, matrix)
            print("The maxtrix: %s is written"% (matrix_name))
        elif command == "show":
            matrix_name = parts[1]
            matrix = dict_matrix[matrix_name]
            show_matrix(matrix)
        elif command == "quit":
            print("program terminated")
        else:
            print("Not an option")


main ()
