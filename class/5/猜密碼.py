import random
r = input(input())
ans = random.randint(1, 100)

for i in range(1, 101):
    print('i')
    if i == ans:
        print('yes')
        break