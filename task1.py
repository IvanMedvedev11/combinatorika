from itertools import permutations
subjects = ['музыка', 'матеша', 'узкий', 'литра', 'история']
ans = list(permutations(subjects, 5))
size = len(ans)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(f'{j+1}. {ans[i][j]}')
    print()
print("Кол-во способов: 120")
