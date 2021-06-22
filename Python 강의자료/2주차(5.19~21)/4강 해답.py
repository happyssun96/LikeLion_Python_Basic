#1번
class Baemin:
    def __init__(self, name, phone, menu):
        self.name = name
        self.phone = phone
        self.menu = menu
    def show(self):
        print("이름:", self.name)
        print("전화번호:", self.phone)
    def top_menu(self):
        print(self.name, "의 대표메뉴는", self.menu, "입니다.")
b1 = Baemin("라이장강","050-7458-6610", "5인세트메뉴")
b2 = Baemin("DD치킨", "070-1111-1111", "반반치킨")
b3 = Baemin("부리또 정거장", "070-2222-2222", "치킨라이스")
b1.show()
b1.top_menu()
b2.show()
b2.top_menu()
b3.show()
b3.top_menu()

"""
#2번
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
# a.setdata(4,2) #-> __init__으로 생성자를 만들었기 때문에 생략 
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class MoreFourCal(FourCal): #클래스 상속 
    def pow(self):
        result = self.first ** self.second
        return result
b = MoreFourCal(3,3)
print(b.pow())

class SafeFourCal(FourCal): #메서드 오버라이딩 
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

c = SafeFourCal(4,0)
print(c.div())
"""