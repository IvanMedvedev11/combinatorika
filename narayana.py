def narayana(arr, prefix, skufix):
    while True:
        if arr[:len(prefix)] == prefix and arr[len(arr) - len(skufix):] == skufix:
            print(arr)
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

arr = list(map(int, input("Введите массив: ").split()))
prefix = list(map(int, input("Введите префикс: ").split()))
skufix = list(map(int, input("Введите скуфикс: ").split()))
print(narayana(arr, prefix, skufix))
