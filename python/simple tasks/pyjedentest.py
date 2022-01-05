def search(array, target):

    left = 0
    right = len(array)
    index = 0


    while left < right:


        index = (left + right) // 2

        if array[index] == target_number:
            return index
        else:
            if array[index] < target_number:
                left = index + 1
            else:
                right = index

    return -1


A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
target_number = 8
index = search(A, target_number)
print(index)