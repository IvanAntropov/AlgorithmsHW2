# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

def HeapSort(array: list) -> None:
    length: int = len(array)
    for i in range(length//2 - 1, -1, -1):
        MakeHeap(array, i, length)
    for i in range(length - 1, 0, -1):
        # Replacer(array, 0, i)
        (array[i], array[0]) = (array[0], array[i])  # O(const)
        MakeHeap(array, 0, i)
           
def MakeHeap(array: list, index: int, size: int) -> None:
    left: int = index*2+ 1
    right: int = index*2 +2
    largest: int = index
    if left < size and array[left] > array[index]: 
        largest = left
    if right < size and array[right] > array[largest]: 
        largest = right
    if largest != index:
        # Replacer(array, largest, index)
        (array[index], array[largest]) = (array[largest], array[index])  # O(const)
        MakeHeap(array, largest, size)
      
           
# def Replacer(array: list, i: int, r: int) -> None:
#     temp = array[i]
#     array[i] = array[r]
#     array[r] = temp

array = [-2, 5, 3, -6, 4, 1, -7, 8, 3, 9, 1, 0, 3, -3, 6, 3, 2, 7, -5, 1, 0, 6, -5, 3, -8, 6, 2, 8]
print(array)
HeapSort(array)
print(array)


#-------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#-------------------------------------------------------------------------------------------------




