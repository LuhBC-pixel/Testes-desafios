def pancakeSort(array):
    lenOfArray = len(array)

    while lenOfArray > 1:
        index = array.index(max(array[0: lenOfArray]))

        array = array[index::-1] + array[index + 1: len(array)]
        array = array[lenOfArray - 1::-1] + array[lenOfArray: len(array)]
        lenOfArray -= 1

    return array

pancake = [3, 5, 2, 1, 7, 6, 4]
print(pancakeSort(pancake))