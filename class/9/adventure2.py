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

def fighting(life, magic, money):
    status= [0, 0, 0, 0]
    up_life = life
    up_magic = magic
    up_money = money
    monster_life = random.randint(2, 5)
    print("Monster Life = %d" % monster_life)
    while True:
        act = input('Use magic attack? y/n:')
        if( act == 'y' and up_magic > 1):
            attack = random.randint(4, 10)
            up_magic -= 1
        else:
            print('Your magic point is not enough!!!')
            print('一般攻擊啟動')
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

def store (life, magic, money):
    status = [0, 0, 0, 0]
    while True:
        act = input('what do you want to buy\n'
                    "'l'/life:\n"
                    "'m'/magic:\n"
                    "'q'/quit:\n")
        if (act == 'q'):
            print('88')
            break
        elif(money < 100):
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
    return status


#main loop
sts=[1, 10, 0, 1000] #是否生存/生命/錢
while True:
    rev=input("Do you want 'c' continue 's'go to the store 'q' quit the game")
    if ( rev == "c" ):
        gen_event = random.randint(1, 3)
        if ( gen_event == 1 ):
            sts[1] = update_life(sts[1])
        if ( gen_event == 2 ):
            sts[3] = update_money(sts[3])
        if ( gen_event == 3 ):
            sts = fighting(sts[1], sts[2], sts[3])
            if( sts[0] == 0 ):
                print("Game Over")
                break
            print("sts = %s" %sts)
    elif ( rev == "q" ):
        print("88")
        break
    elif ( rev == "s" ):
        sts=store(sts[1], sts[2], sts[3])
        print("%s" % sts)
    else:
        continue