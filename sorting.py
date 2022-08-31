

def bubble_sort(arr: list[int]):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr: list[int]):
    n = len(arr)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]


def insertion_sort(arr: list[int]):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1



arr = [1]
insertion_sort(arr)
print(arr)
 