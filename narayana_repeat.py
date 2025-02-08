from time import perf_counter
def time_count(function):
    def wrapper(*args, **kwargs):
        tic  = perf_counter()
        function(*args, **kwargs)
        toc = perf_counter()
        print(f"Время работы: {toc - tic}")
    return wrapper

@time_count
def narayana(arr, cnts):
    arr = list(arr)
    cnt = 0
    arr_list = []
    for elem in arr:
        arr_list.extend([elem] * cnts[elem])
    arr = sorted(arr_list)
    while True:
        print(*arr)
        cnt += 1
        index_i = 0
        index_j = 0
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                index_i = i
                break
        else:
            print(cnt)
            return ""
        for j in range(len(arr)-1, -1, -1):
            if arr[j] > arr[index_i]:
                index_j = j
                break
        arr[index_i], arr[index_j] = arr[index_j], arr[index_i]
        arr[index_i+1:] = arr[:index_i:-1]
arr = input("Введите слово: ")
cnts = {}
arr_set = set(arr)
for elem in arr_set:
    cnts[elem] = arr.count(elem)

narayana(arr_set, cnts)
