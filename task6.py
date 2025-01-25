from itertools import product
from time import perf_counter
def generate_numbers(digits, length):
    return [int(''.join(map(str, combo))) for combo in product(digits, repeat=length)]
def my_generate(digits):
    nums = []
    for el1 in digits:
        for el2 in digits:
            for el3 in digits:
                nums.append(el1 * 100 + el2 * 10 + el3)
    return nums
digits = [1, 3, 9]
tic = perf_counter()
res = []
nums = list(map(int, generate_numbers(digits, 3)))  # Генерация трехзначных чисел
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] >= 550:
            res.append(nums[i] + nums[j])
print(res)
toc = perf_counter()
print(toc - tic)
tic = perf_counter()
res = []
nums = my_generate(digits)  # Генерация трехзначных чисел
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] >= 550:
            res.append(nums[i] + nums[j])
print(res)
toc = perf_counter()
print(toc - tic)
