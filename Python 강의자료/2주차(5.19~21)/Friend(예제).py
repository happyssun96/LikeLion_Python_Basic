class Friend: #클래스 연습문제 정답
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print("이름 :" + self.name)
        print("전화번호 : " + self.phone)
f1 = Friend("김xx", "010-0100-0101")
f2 = Friend("정xx", "010-0101-2222")
f3 = Friend("강xx", "010-0100-3333")
f1.show()
f2.show()
f3.show()
