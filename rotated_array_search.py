import random


def list_generator(length, start, stop, sortnum = "Yes"):
    num_set = set()
    while len(num_set) < length :
        num_set.add(random.randrange(start, stop))
    ro_list = list(num_set)
    if sortnum == "Yes" :
        ro_list.sort()
    # print(ro_list)
    return ro_list
# list_generator(100, 1, 1011)


def list_rotater(got_list):
    # list = [5, 10, 25, 45, 51]
    x = random.randrange(0, len(got_list))
    
    rotated_list = []
    rotated_list = got_list[x:] + got_list[0:x]

    if x != 0 : return rotated_list, len(got_list) - x 
    else : return rotated_list, 0
    # print(rotated_list)

        
# list_rotater(4)

def times_rotated(ro_list, re_list = [], isort = "Yes"):
    # list11 = [1,5,7,10,15]
    # ro_list = [7,10,15,1,5]
    # re_list = [5,51,7,15,21]
    # ro_list = [7,15,21,5,51]

    if isort.capitalize() == "Yes" :
        no_rotate = (len(ro_list) - ro_list.index(max(ro_list))) - 1

    elif isort.capitalize() == "No" :
        no_rotate = len(re_list) - ro_list.index(re_list[0]) if ro_list.index(re_list[0]) != 0 else 0
    # print(no_rotate)
    return(len(ro_list) - no_rotate) if no_rotate != 0 else no_rotate

# print(times_rotated([7,10,15,1,5], [], "no"))

def ro_binary(ro_list):
    # ro_list = [7,10,15,1,5]
    # ro_list = [51, 71, 75, 81, 82, 88, 95, 1, 5, 7, 11, 15, 25, 31, 35, 41, 45]
    start = 0
    end = len(ro_list)
    i = 0
    while True :
        i += 1
        num_search = (start + end)//2 
        num = ro_list[num_search]
        if num > ro_list[start] :
            start = num_search
        elif num < ro_list[start] :
            end = num_search
        elif num == ro_list[start] :
            break
        # print(num_search, num)
    # print(num_search)
    # print(len(ro_list))
    if len(ro_list) == (num_search + 1) : return 0 , i, len(ro_list)
    else : return (num_search + 1), i, len(ro_list)
        
print(ro_binary(ro_list = [7]))



def ro_run_all(times, sorted = "Yes"):
    times_win = 0
    times_lose = 0
    if sorted == "Yes":
        for i in range(times) :
            list_generated = list_generator(100,1,10000)
            list_rotated = list_rotater(list_generated)
            # print(list_generated)
            # print(list_rotated)
            result = times_rotated(list_rotated[0])
            # print(result)
            if list_rotated[1] == result :
                times_win += 1
            else : times_lose += 1
    if sorted.capitalize() == "No" :
        for i in range(times) :
            list_generated = list_generator(100,1,1000, "No")
            list_rotated = list_rotater(list_generated)
            # print(list_generated)
            # print(list_rotated)
            result = times_rotated(list_rotated[0], list_generated, isort= "No")
            # print(result)
            if list_rotated[1] == result :
                times_win += 1
            else : times_lose += 1

    print(f"Number of times won : {times_win} and loss : {times_lose}")

# ro_run_all(1000, "Yes")

def run_all_bin(times, sorted = "Yes"):
    times_win = 0
    times_lose = 0
    total_iterations = 0
    iterations_per_list = 0
    if sorted == "Yes":
        for i in range(times) :
            list_generated = list_generator(100,1,10000)
            list_rotated = list_rotater(list_generated)
            # print(list_generated)
            # print(list_rotated)
            result = ro_binary(list_rotated[0])
            # print(result)
            if list_rotated[1] == result[0] :
                times_win += 1
                total_iterations += result[1]
                iterations_per_list += result[1]/result[2]

            else : times_lose += 1
            avg_iterations = total_iterations/times
            avg_iterations_per_list = iterations_per_list/times
    
    print(f"Number of times won : {times_win} and loss : {times_lose} and average iterations : {avg_iterations} average iterations per data size : {avg_iterations_per_list}")

run_all_bin(1000, "Yes")