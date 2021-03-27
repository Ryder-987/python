"""
Topic:輸入溫度，如果溫度>=40度C,顯示: 太熱,
　　　如果溫度<= 10 顯示:太冷, 其他：舒適:

Show:Please input temperature:"
Input1:40
Output:It's too hot.
"""

temperature=input('Please input temperature:')
temperature=int(temperature)
if (temperature>=40):
    print("It's too hot.")
elif (temperature<=10):
    print("It's too cold.")
else:
    print('comfortable')