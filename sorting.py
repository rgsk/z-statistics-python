# nodemon --watch sorting.py -e py --exec "mypy sorting.py && python sorting.py"


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


def merge(arr: list[int], start: int, mid: int, end: int):

    temp_arr = [0] * (end - start + 1)
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= end:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for i in range(start, end + 1):
        arr[i] = temp_arr[i - start]


def merge_sort_helper(arr: list[int], start: int, end: int):
    if start < end:
        mid: int = (start + end) // 2
        merge_sort_helper(arr, start, mid)
        merge_sort_helper(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge_sort(arr: list[int]):
    merge_sort_helper(arr, 0, len(arr) - 1)


arr = [10, 1, 2, 7, 6, 1, 5]
merge_sort(arr)
print(arr)
