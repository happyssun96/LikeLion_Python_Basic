# if 문
heat = float(input("temperture ??"))
corona = None

if heat >= 38.5 and corona == True:
    print("격리")
elif heat >= 38.5:
    print("진단검사")
else:
    print("통과")

# for 문
solar_system = ["태양","수성","금성",'지구',"화성","목성","토성","천왕성","해왕성"]

for stars in solar_system:
    print(stars)

# while 문
'''
ILoveU = True
while ILoveU == True:
    print("I love you forever")
'''
# 함수

users = [
    {"name":"SKT T1 Faker", "online": True, "match_making": True},
    {"name":"SKT T1 Teddy", "online": True, "match_making": True},
    {"name":"SKT T1 Bengi", "online": False,"match_making": False},
    ]

game_users = []

def start_game():
    print("Game Start")

def online_user_print(users):
    for user in users:
        if user["online"] == True:
            print(user["name"] + " is online.")
        else:
            print(user["name"] + " is offline.")

def make_monseter():
    monster = {"name": "Blue Sentinel", "hp": 2100, "damage": 82}
    return monster

def game_match(users, gmae_users):
    for user in users:
        if user["online"] == True and user["match_making"] == True:
            game_users.append(user)
        else:
            pass

start_game()

online_user_print(users)

gen = make_monseter()
print(gen["name"]+'이 소환 되었습니다.')


print(game_users)
game_match(users, game_users)
print(game_users)

# 클래스

class LionTalk:
    def __init__(self, opponent):
        self.text = ""
        print(opponent,"와(과) 채팅중입니다.")

    def texting(self):
        self.text = input()

    def send(self):
        print("나: "+self.text)
        self.text = ""



opp = input("채팅할 상대: ")
room1 = LionTalk(opp)
room1.texting()
room1.send()

