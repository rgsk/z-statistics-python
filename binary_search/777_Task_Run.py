# nodemon --watch 777_Task_Run.py -e py --exec "mypy 777_Task_Run.py && python 777_Task_Run.py"
def solve1(tasks: list[int], k: int):
    last_times: dict[int, int] = {}
    cur_time = 0
    for task in tasks:
        if task in last_times and cur_time - last_times[task] <= k:
            waiting_time = k - (cur_time - last_times[task]) + 1
            cur_time += waiting_time
        last_times[task] = cur_time
        cur_time += 1
    return cur_time


def test1():
    tasks1 = [0, 1, 0, 0, 1]
    k1 = 2
    print(solve1(tasks1, k1))


test1()
 