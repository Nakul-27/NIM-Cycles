import math

def basic(a, b, operation):
    print("a = ", a)
    print("b = ", b)
    if operation == "add":
        c = b + b
    elif operation == "mult":
        c = a * b
    else:
        print("Unreachable!")
    # c = a + b
    print("c = ", c)
    # print("Proposed Cycle Length (c + a): ", c + a)

    max_num = max(a,max(b,c))
    starting_index = max_num

    final_array = [0] * 200

    for index in range(starting_index, len(final_array)):
        prod = final_array[index - a] * final_array[index - b] * final_array[index - c]
        final_array[index] = (prod + 1) % 2

    return final_array

if __name__ == "__main__":
    f = open("output.txt", "w+")
    f.writelines("Conjecture: When c = a + b, then the cycle length is equal to c + a.\n")
    a = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    b = [1,2,3,4,5]
    for elem in a:
        for elemen in b:
            f.writelines("a = ")
            f.writelines(str(elem))
            f.writelines("\n")
            f.writelines("b = ")
            f.writelines(str(elemen))
            f.writelines("\n")
            f.writelines("c = ")
            f.writelines(str(elemen + elemen))
            f.writelines("\n")
            f.writelines("\n")
            f.writelines(str(basic(elem, elemen, "add")))
            f.writelines("\n\n")
