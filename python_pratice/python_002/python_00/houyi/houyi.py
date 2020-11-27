from python_pratice.python_002.python_00.python_game import Game


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
                elif:
                    raise  Exception("不要平局")
                    print("平了")


houyi = HouYi(2000, 1000)
houyi.fight()


