def fight():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power

        if (my_hp <= 0 ):
            print("我的血量是：" , my_hp)
            print("你的血量是：" , your_hp)
            print("w我输了")
            break

        elif(your_hp<=0):
            print("我的血量是：",my_hp)
            print("你的血量是：",your_hp)
            print("你输了")
            break

  
   
fight()


