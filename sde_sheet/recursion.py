# nodemon --watch recursion.py -e py --exec "mypy recursion.py && python recursion.py"


from calendar import c
import itertools
from math import factorial


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


def combination_sum_2_helper(arr: list[int], remaining_target: int, index: int, current_list: list[int], final_ans: list[list[int]]):
    if remaining_target == 0:
        cur_copy = current_list.copy()
        if cur_copy not in final_ans:
            final_ans.append(cur_copy)
        return
    n = len(arr)
    if index == n:
        return

    # include
    current_list.append(arr[index])
    combination_sum_2_helper(
        arr, remaining_target - arr[index], index + 1, current_list, final_ans)
    current_list.pop()
    # exclude
    combination_sum_2_helper(
        arr, remaining_target, index + 1, current_list, final_ans)


def combination_sum_2(arr: list[int], target: int):
    final_ans: list[list[int]] = []
    current_list: list[int] = []
    combination_sum_2_helper(sorted(arr), target, 0, current_list, final_ans)
    return final_ans


def get_combination_sum_2_optimized_helper(index: int, arr: list[int], current_arr: list[int], final_ans: list[list[int]], cur_sum: int, target: int):
    arr_copy = current_arr.copy()
    if cur_sum == target:
        final_ans.append(arr_copy)
    for i in range(index, len(arr)):
        if (i != index and arr[i] == arr[i-1]):
            continue
        current_arr.append(arr[i])
        get_combination_sum_2_optimized_helper(
            i + 1, arr, current_arr, final_ans, cur_sum + arr[i], target)
        current_arr.pop()


def get_combination_sum_2_optimized(arr: list[int], target: int):
    final_ans: list[list[int]] = []
    current_arr: list[int] = []
    get_combination_sum_2_optimized_helper(
        0, sorted(arr), current_arr, final_ans, 0, target)
    return final_ans


def test_combination_sum_2():
    arr1 = [2, 3, 6, 7, 5]
    target1 = 8
    print(get_combination_sum_2_optimized(arr1, target1))
    arr2 = [2]
    target2 = 1
    print(get_combination_sum_2_optimized(arr2, target2))
    arr3 = [3, 9, 10, 16, 1, 15, 2]
    target3 = 21
    print(get_combination_sum_2_optimized(arr3, target3))
    arr4 = [10, 1, 2, 7, 6, 1, 5]
    target4 = 8
    print(get_combination_sum_2_optimized(arr4, target4))
    arr5 = [2, 5, 2, 1, 2]
    target5 = 5
    print(get_combination_sum_2_optimized(arr5, target5))


def is_palindrome(items: list | str, start: int, end: int):
    while start < end:
        if items[start] != items[end]:
            return False
        start += 1
        end -= 1
    return True


def palindrome_partitioning_helper(s: str, index: int, cur_partitions: list[str], final_ans: list[list[str]]):
    if index == len(s):
        copied = cur_partitions.copy()
        final_ans.append(copied)
        return

    for i in range(index, len(s)):
        if (is_palindrome(s, index, i)):
            partition = s[index: i+1]
            cur_partitions.append(partition)
            palindrome_partitioning_helper(s, i+1, cur_partitions, final_ans)
            cur_partitions.pop()


def palindrome_partitioning(s: str):
    cur_partitions: list[str] = []
    final_ans: list[list[str]] = []
    palindrome_partitioning_helper(s, 0, cur_partitions, final_ans)
    return final_ans


def test_palindrome_partitioning():
    s1 = 'aab'
    print(palindrome_partitioning(s1))
    s2 = 'aabb'
    print(palindrome_partitioning(s2))


def find_kth_permutation(n: int, k: int):
    perms = list(itertools.permutations(range(1, n+1)))
    return "".join([str(v) for v in perms[k-1]])


def find_kth_permutation_optimized_helper(n: int, k: int, ans: list[int], index: int, perms: list[int]):
    if index == len(ans):
        return
    one_less_factorial = factorial(n - 1)
    index_choosen = k // one_less_factorial if k / \
        one_less_factorial > k // one_less_factorial else k // one_less_factorial - 1
    ans[index] = perms[index_choosen]
    perms.pop(index_choosen)
    find_kth_permutation_optimized_helper(
        n-1, k - index_choosen * one_less_factorial, ans, index + 1, perms)


def find_kth_permutation_optimized(n: int, k: int):
    ans: list[int] = [0] * n
    perms = [i+1 for i in range(n)]
    find_kth_permutation_optimized_helper(n, k, ans, 0, perms)
    return ans


def test_find_kth_permutation():
    # print(find_kth_permutation_optimized(3, 1))

    for i in range(1, 25):
        print(find_kth_permutation_optimized(4, i))


test_find_kth_permutation()

'''
3
1, 2, 3, 4
5

'''
