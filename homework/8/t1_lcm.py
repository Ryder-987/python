'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''

def lcm(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i

num1 = int(input(""))
num2 = int(input(""))
print(lcm(num1, num2))