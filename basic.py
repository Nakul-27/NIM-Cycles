# Basic implementation of NIM in Python
# Further information in "NIM Cycles.xlsx"
# Nakul Rao
import math

def play(a, b, operation):
    if operation == "add":
        c = b + b
    elif operation == "mult":
        c = b * b
    else:
        print("Invalid Operation")
        exit()

    max_num = max(a,max(b,c))
    starting_i = max_num

    final_array = [0] * 400
    length = len(final_array)

    for n in range(starting_i, length):
        prod = final_array[n - a] * final_array[n - b] * final_array[n - c]
        final_array[n] = (prod + 1) % 2

    return final_array

def write_to_file(file_name, a, b):
    f = open(file_name, "w")
    for element_a in a:
        for element_b in b:
            f.writelines("a = ")
            f.writelines(str(element_a))
            f.writelines("\n")
            f.writelines("b = ")
            f.writelines(str(element_b))
            f.writelines("\n")
            f.writelines("c = ")
            f.writelines(str(element_b + element_b))
            f.writelines("\n")
            f.writelines("\n")
            f.writelines(str(play(element_a, element_b, "add")))
            f.writelines("\n\n")
    print("Written.")

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    b = [1,2,3,4,5]
    write_to_file("output.txt", a, b)

