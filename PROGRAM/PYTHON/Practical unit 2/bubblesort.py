def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            # To sort in descending order, change > to < in this line.
            if array[j] > array[j + 1]:
                # swap if greater is at the rear position
                (array[j], array[j + 1]) = (array[j + 1], array[j])

        data = [-2, 45, 0, 11, -9]
        bubbleSort(data)
        print('Sorted Array in Asc ending Order:')
        print(data)
def bubble_sort(list1):
    # We can stop the iteration once the swap has done
    has_swapped = True
    while (has_swapped):
        has_swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    return list1
list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))

'''The unsorted list is:  [5, 3, 8, 6, 7, 2]
The sorted list is:  [2, 3, 5, 6, 7, 8]'''