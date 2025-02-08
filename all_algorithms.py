import itertools
from time import perf_counter
def time_count(function):
    def wrapper(*args, **kwargs):
        tic  = perf_counter()
        function(*args, **kwargs)
        toc = perf_counter()
        print(f"Время работы: {toc - tic}")
    return wrapper
@time_count
def johnson_trotter(arr):
    print(*arr)
    directions = {}
    combos = []
    for i in range(len(arr)):
        directions[arr[i]] = -1
    mobile_element = 0
    while True:
        for i in range(len(arr)):
            if 0 <= i + directions[arr[i]] < len(arr) and arr[i] > arr[i + directions[arr[i]]] and arr[i] > mobile_element:
                mobile_element = arr[i]
        if mobile_element == 0:
            for combo in combos:
                print(*combo)
            return ""
        for i in range(len(arr)):
            if arr[i] == mobile_element:
                if 0 <= i + directions[mobile_element] < len(arr):
                    arr[i], arr[i + directions[mobile_element]] = arr[i + directions[mobile_element]], arr[i]
                break
        combos.append(tuple(arr))
        for i in range(len(arr)):
            if arr[i] > mobile_element:
                directions[arr[i]] = -directions[arr[i]]
        mobile_element = 0
@time_count
def narayana(arr):
    while True:
        print(*arr)
        index_i = 0
        index_j = 0
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                index_i = i
                break
        else:
            return ""
        for j in range(len(arr)-1, -1, -1):
            if arr[j] > arr[index_i]:
                index_j = j
                break
        arr[index_i], arr[index_j] = arr[index_j], arr[index_i]
        arr[index_i+1:] = arr[:index_i:-1]
@time_count
def itertools_function(arr):
    perms = itertools.permutations(arr)
    for perm in perms:
        print(*perm)
arr = [1, 2, 3, 4, 5]
arr1 = arr.copy()
arr2 = arr.copy()
johnson_trotter(arr)
narayana(arr1)
itertools_function(arr2)
