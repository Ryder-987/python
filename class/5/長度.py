d = int(input())
cnt = 0

while d >= 20 :
    d /= 2
    cnt += 1
    print(d)
else:
    print('共折了:' ,cnt, '次')