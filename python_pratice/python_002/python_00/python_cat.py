##定义类
class Cat:
    ##属性
    color = "ororange"
    leg = 4

    def eat(self):
        print("吃")

    def cry(self):
        print("叫")

print(Cat.color)

cat = Cat()

print(cat.color)
print(cat.eat())



