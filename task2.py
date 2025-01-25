from itertools import permutations
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
arr = [1, 3, 7]
ans = list(permutations(arr))
size = len(ans)
for i in range(len(ans)):
    print("".join(list(map(str, ans[i]))))
print(f"Кол-во способов: {factorial(len(arr))}")
