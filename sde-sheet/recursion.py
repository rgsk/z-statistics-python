# nodemon --watch recursion.py -e py --exec "mypy recursion.py && python recursion.py"

def get_subset_sums_helper(arr: list[int], index: int, current_sum: int, final_ans: list[int]):
    n = len(arr)
    if index == n:
        final_ans.append(current_sum)
        return
    # include
    get_subset_sums_helper(arr, index + 1, current_sum + arr[index], final_ans)
    # exclude
    get_subset_sums_helper(arr, index + 1, current_sum, final_ans)


def get_subset_sums(arr: list[int]):
    final_ans: list[int] = []
    get_subset_sums_helper(arr, 0, 0, final_ans)
    return sorted(final_ans)


def test_get_subset_sums():
    arr1 = [3, 1, 2]
    print(get_subset_sums(arr1))
    arr2 = [5, 2, 1]
    print(get_subset_sums(arr2))


def get_subsets_helper(arr: list[int], index: int, current_arr: list[int], final_ans: list[list[int]]):
    n = len(arr)
    if index == n:
        copied = current_arr.copy()
        if copied not in final_ans:
            final_ans.append(copied)
        return

    # include
    current_arr.append(arr[index])
    get_subsets_helper(
        arr, index + 1, current_arr, final_ans)
    current_arr.pop()
    # exclude
    get_subsets_helper(arr, index + 1, current_arr, final_ans)


def get_subsets(arr: list[int]):
    final_ans: list[list[int]] = []
    current_arr: list[int] = []
    get_subsets_helper(arr, 0, current_arr, final_ans)
    return sorted(final_ans)


def get_subsets_optimized_helper(index: int, arr: list[int], current_arr: list[int], final_ans: list[list[int]]):
    final_ans.append(current_arr.copy())
    for i in range(index, len(arr)):
        if (i != index and arr[i] == arr[i-1]):
            continue
        current_arr.append(arr[i])
        get_subsets_optimized_helper(i + 1, arr, current_arr, final_ans)
        current_arr.pop()


def get_subsets_optimized(arr: list[int]):
    final_ans: list[list[int]] = []
    current_arr: list[int] = []
    get_subsets_optimized_helper(0, arr, current_arr, final_ans)
    return final_ans


def test_get_subsets():
    arr1 = [1, 2, 3]
    print(get_subsets_optimized(arr1))
    arr2 = [1, 2, 2]
    print(get_subsets_optimized(arr2))
    arr3 = [1]
    print(get_subsets_optimized(arr3))
    arr4 = [2, 2, 2]
    print(get_subsets_optimized(arr4))


def combination_sum_1_helper(arr: list[int], remaining_target: int, index: int, current_map: dict[int, int], final_ans: list[list[int]]):
    if remaining_target == 0:
        solution: list[int] = []
        for (value, times) in current_map.items():
            for i in range(times):
                solution.append(value)
        final_ans.append(solution)
        return
    n = len(arr)
    if index == n:
        return
    for i in range(remaining_target//arr[index] + 1):
        current_map[arr[index]] = i
        combination_sum_1_helper(
            arr, remaining_target - arr[index] * i, index + 1, current_map, final_ans)


def combination_sum_1(arr: list[int], target: int):
    final_ans: list[list[int]] = []
    current_map: dict[int, int] = {}
    combination_sum_1_helper(arr, target, 0, current_map, final_ans)
    return final_ans


def test_combination_sum_1():
    arr1 = [2, 3, 6, 7]
    target1 = 8
    print(combination_sum_1(arr1, target1))
    arr2 = [2]
    target2 = 1
    print(combination_sum_1(arr2, target2))
    arr3 = [3, 9, 10]
    target3 = 19
    print(combination_sum_1(arr3, target3))


test_combination_sum_1()
