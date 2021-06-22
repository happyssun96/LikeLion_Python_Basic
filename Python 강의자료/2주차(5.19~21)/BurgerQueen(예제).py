class BurgerQueen: #클래스 강의자료 응용
    count = 0
    def __init__(self, size, menu):
        self.size = size
        self.menu = menu
        BurgerQueen.count += 1
    def print(self):
        print("사이즈 : " + self.size)
        print("메뉴 : " + self.menu)
    def price(self):
        if self.size == 'L':
            print("6000원 입니다")
        elif self.size == 'M':
            print("4000원 입니다")
        else:
            print("3000원 입니다")
b1 = BurgerQueen("L", "새우버거")
b2 = BurgerQueen("M", "치즈버거")
b3 = BurgerQueen("S", "불고기버거")
b4 = BurgerQueen("L", "치킨버거")
print("<<버거퀸에 어서오세요>>")
print(BurgerQueen.count, '가지 종류가 있어요')
b1.print()
b1.price()
print("============")
b2.print()
b2.price()
print("============")
b3.print()
b3.price()
print("============")
b4.print()
b4.price()
