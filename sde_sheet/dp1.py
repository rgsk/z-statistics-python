# nodemon --watch dp1.py -e py --exec "mypy dp1.py && python dp1.py"


def max_product_subarray(arr: list[int]):
    n = len(arr)
    max_product = -1000000
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            max_product = max(max_product, product)
    return max_product


def max_product_subarray1(arr: list[int]):
    res = arr[0]
    cur_max = 1
    cur_min = 1
    for v in arr:
        if v == 0:
            cur_max, cur_min = 1, 1
            continue
        temp = cur_max * v
        cur_max = max(temp, v * cur_min, v)
        cur_min = min(temp, v * cur_min, v)
        res = max(res, cur_max)
    return res


def test_max_product_subarray():
    arr1 = [1, 2, 3, 4, 5, 0]
    print(max_product_subarray1(arr1))
    arr2 = [1, 2, -3, 0, -4, -5]
    print(max_product_subarray1(arr2))


test_max_product_subarray()
