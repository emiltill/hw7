def bubble_sort(chaos):
    size = len(chaos)
    swap = 0
    index = size - 1
    for i in range(index):
        for k in range(0, index - i):
            if chaos[k] > chaos[k + 1]:
                swap = chaos[k]
                chaos[k] = chaos[k + 1]
                chaos[k + 1] = swap

    print(chaos)


anarchy = [23, 76, 3, 11, 54, 98, 32, 49, 5, 7, 899, 354]
bubble_sort(anarchy)
