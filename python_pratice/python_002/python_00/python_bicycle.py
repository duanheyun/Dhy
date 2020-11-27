class Bicycle:
    def run(self, km):
        print(f"一共骑了{km}km")

#bike = Bicycle()
#bike.run(100)
#继承父类
class Ebicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume
    # 电动车充了多少电
    def fill_change(self, vol):
        print(f"充了{vol}电")
        print(f"充完电之后 还有{vol+self.valume}电")
        self.valume = self.valume+ vol

    def run(self, km):
        e_km = self.valume*10
        print(f"{e_km}")

        if km <= e_km:
            print(f"用电骑行了{km}km")
        else:
            print(f"用脚骑了{km - e_km}KM")


ebike = Ebicycle(1000)
ebike.fill_change(10000)
ebike.run(10000000)