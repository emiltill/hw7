def binary_search(num, num_list):
    num_list = sorted(num_list)
    print(num_list)
    first = 0  # index
    length = len(num_list)
    last = length - 1  # index
    middle_index = (first + last) // 2  # index
    middle = num_list[middle_index] # value

    while True:
        if first == last:
            if middle != num:
                print("The number was not found in the list")
                break

        elif middle == num:
            print(f"Index of {middle} is {middle_index}")
            break

        elif middle > num:
            high = middle_index - 1
            last = high
            middle_index = (first + last) // 2
            middle = num_list[middle_index]
            if middle == num:
                print(f"Index of {middle} is {middle_index}")
                break

        elif middle < num:
            low = middle_index + 1
            first = low
            last = length - 1
            middle_index = (first + last) // 2
            middle = num_list[middle_index]
            if middle == num:
                print(f"Index of {middle} is {middle_index}")
                break


numbers = [6, 99, 45, 34, 78, 16, 33, 51, 67]
binary_search(99, numbers)
