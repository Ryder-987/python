"""
Topic:輸入分子及分母，確認是否等於 350/450:

Show:Please input numerator"
Input1:70

show:Please input Denominator:
Input2:90
Output:True

Input1:6
Input2:9
Output:False
"""

check = 350 / 450
numerator=input('Please input numerator:')
Denominator=input('Please input Denominator:')
if (numerator=='70') & (Denominator=='90'):
    print('True')
else:
    print('False')