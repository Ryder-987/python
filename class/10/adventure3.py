'''
新增防具:防具提供，防護點數，受到攻擊先扣防護點數，防護點數不夠才扣血量
商店賣武器:可加一般攻擊
新增武器:武器可以增加一般攻擊力
新增防具:防具提供，防護點數，受到攻擊先扣防護點數，防護點數不夠才扣血量
'''
from PIL import Image
import time
import random

def close_game(sts):
    path = 'output.txt'
    f = open(path, 'w')
    for i in range(len(sts)):
        f.write(str(sts[i]) + "\n")
    f.close()
def read_file():
    path = 'output.txt'
    f = open(path, 'r')
    text = []
    for line in f:
        text.append(int(line))
    print(text)
    f.close()
    return text
def update_life(life):
  get_life = random.randint(1, 3)
  new_life = life + get_life
  print("Your recovry Life = %d Your life %d" % (get_life, new_life))
  return new_life

def update_money(money):
  get_money = random.randint(30, 50)
  new_money = money + get_money
  print("Your Get Money = %d Your Money =%d" % (get_money, new_money))
  return new_money

def fighting(life, magic, money, katana):
    status= [0, 0, 0, 0, 0]
    up_life = life
    up_magic = magic
    up_money = money
    monster_life = random.randint(2, 5)
    print("Monster Life = %d" % monster_life)

    while True:
        act = input('Use magic attack , regular attack or katana? m/r/k:')
        if( act == 'm' and up_magic > 1):
            attack = random.randint(4, 10)
            up_magic -= 1
        elif( act == 'k' and katana == 1):
            filename = 'price.jpg'
            img = Image.open(filename)
            img.show()
            attack = random.randint(50, 100)
            katana -= 1
        else:
            print('使出一般攻擊、魔力點數未滿 或 錢不夠使用武士刀(k)!')
            attack = random.randint(1, 3)
        print("You make damage %d" % attack)
        monster_life -= attack
        time.sleep(1)
        print("Monster Life %d" % monster_life)
        if (monster_life < 1):
            print("You beat monster")
            up_money += + random.randint(10, 20)
            status[0] = 1
            status[1] = up_life
            status[2] = up_magic
            status[3] = up_money
            return status
        print("Monster Attack")
        time.sleep(1)
        up_life -= 3
        print("You get hurt, Life=%d" % up_life)
        if ( up_life <= 0):
            print("You dead \n")
            status[0] = 0
            status[1] = up_life
            status[2] = up_magic
            status[3] = up_money
            return status

def store (life, magic, money, katana):
    status = [0, 0, 0, 0, 0]
    while True:
        act = input('what do you want to buy\n'
                    "'l'/life:\n"
                    "'m'/magic:\n"
                    "'k'/katana:\n"
                    "'q'/quit:\n")
        if (act == 'q'):
            print('88')
            break
        elif(act == 'k' and money >= 10000):
            katana += 1
            money -= 10000
            print(' katana= %d Money = %d' % (katana, money))
        elif(money < 100) or (act == 'k' and money <= 10000):
            print('Money is not enough , quit store')
            break
        elif(act == 'l'):
            life += random.randint(1, 3)
            money -= 100
            print('Life = %d Money = %d' % (life, money))
        elif(act == 'm'):
            magic += random.randint(2, 6)
            money -= 100
            print('Magic = %d Money = %d' % (magic, money))
        else:
            continue
    status[0] = 1
    status[1] = life
    status[2] = magic
    status[3] = money
    status[4] = katana
    return status


#main loop
#sts=[1, 10, 0, 10000, 0] #是否生存/生命/錢/武士刀
sts = read_file()
while True:
    rev=input("Do you want 'c' continue 's'go to the store 'q' quit the game")
    if ( rev == "c" ):
        gen_event = random.randint(1, 3)
        if ( gen_event == 1 ):
            sts[1] = update_life(sts[1])
        if ( gen_event == 2 ):
            sts[3] = update_money(sts[3])
        if ( gen_event == 3 ):
            sts = fighting(sts[1], sts[2], sts[3], sts[4])
            if( sts[0] == 0 ):
                print("Game Over")
                break
            print("sts = %s" %sts)
    elif ( rev == "q" ):
        print("88")
        close_game(sts)
        break
    elif ( rev == "s" ):
        sts=store(sts[1], sts[2], sts[3], sts[4])
        print("%s" % sts)
    else:
        continue