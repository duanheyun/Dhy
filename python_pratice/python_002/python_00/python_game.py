class Game:
    def __init__(self, my_hp, your_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.your_hp = your_hp
        self.your_power = 199

    def fight(self):
            while True:
                self.my_hp = self.my_hp - self.your_power
                self.your_hp = self.your_hp - self.my_power

                if (self.my_hp <= 0):
                    self.my_hp = 0
                    print("我的血量是：", self.my_hp)
                    print("你的血量是：", self.your_hp)
                    print("w我输了")
                    break


                elif (self.your_hp <= 0):
                    self.your_hp = 0
                    print("我的血量是：", self.my_hp)
                    print("你的血量是：", self.your_hp)
                    print("你输了")
                    break




#game = Game(2000,1000)
#game.fight()

class HouYi(Game):
    def __init__(self, houyi_hp, your_hp):
        #继承父类构造方法
        super().__init__(houyi_hp,your_hp= your_hp)
        self.defence = 1000

    def fight(self):
            while True:
                self.my_hp = self.my_hp + self.defence - self.your_power
                self.your_hp = self.your_hp - self.my_power

                if (self.my_hp <= 0):

                    print("我的血量是：", self.my_hp)
                    print("你的血量是：", self.your_hp)
                    print("w我输了")
                    break


                elif (self.your_hp <= 0):

                    print("我的血量是：", self.my_hp)
                    print("你的血量是：", self.your_hp)
                    print("你输了")
                    break

houyi = HouYi(2000, 1000)
houyi.fight()


