'''
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。
'''

n = int (input('n'))
for i in range(2 , n+1):
    for j in range(2 ,i):
        if (i % j == 0):
            break
    else:
        print(i)