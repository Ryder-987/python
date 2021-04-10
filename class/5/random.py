import random
d = 0
cnt = 0
random.randint(2, 6)


while d != 5 :
    d=random.randint(1,6)
    cnt+=1
    print(d)
else:
    print('恭喜中獎!/n共抽了:' ,cnt, '次')