def isSorted(elements):
    cantidad = len(elements)
    for i in range (cantidad - 1):
        if elements [i] > elements[i + 1]:
            return False
    return True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(isSorted(numbers))