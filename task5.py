from itertools import product

def generate_numbers(digits, length):
    return [int(''.join(map(str, combo))) for combo in product(digits, repeat=length)]

digits = [1, 3, 9]
res = []
nums = list(map(int, generate_numbers(digits, 3)))  # Генерация трехзначных чисел
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] >= 550:
            res.append(nums[i] + nums[j])
print(res)
