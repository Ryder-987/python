'''
尋問用魔法/普通攻擊
增加魔法攻擊(4-8點攻擊力)，每次需使用1點魔力
新增商店(m(回魔)/l(回血)/q(離開))
  回魔藥水，一瓶100元/2-4點魔力，錢不夠無法購買
  回血藥水，一瓶100元/3-6點體力，錢不夠無法購買
'''

import time
import random

def update_life(life):
  get_life = random.randint(1, 3)
  new_life = life + get_life
  print("Your recovry Life = %d Your life %d" % (get_life, new_life))
  return new_life

def update_money(money):
  get_money = random.randint(10, 30)
  new_money = money + get_money
  print("Your Get Money = %d Your Money =%d" % (get_money, new_money))
  return new_money

def fighting(life, money):
    status= [0, 0, 0]
    up_life = life
    up_money = money
    monster_life = random.randint(2, 5)
    print("Monster Life = %d" % monster_life)
    while True:
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
            status[2] = up_money
            return status
        print("Monster Attack")
        time.sleep(1)
        up_life -= 3
        print("You get hurt, Life=%d" % up_life)
        if ( up_life <= 0):
            print("You dead \n")
            status[0] = 0
            status[1] = up_life
            status[2] = up_money
            return status
sts=[1, 10 , 0] #是否生存/生命/錢
while True:
    rev=input("Do you want 'c' continue 'q' quit the game")
    if ( rev == "c" ):
        gen_event = random.randint(1, 3)
        if ( gen_event == 1 ):
            sts[1] = update_life(sts[1])
        if ( gen_event == 2 ):
            sts[2] = update_money(sts[2])
        if ( gen_event == 3 ):
            sts = fighting(sts[1], sts[2])
            if( sts[0] == 0 ):
                print("Game Over")
                break
            print("sts = %s" %sts)
    elif ( rev == "q" ):
        print("see you")
        break
    else:
        continue
