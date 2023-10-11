import random
Deck = []
List_Colour = ['Spade','Heart','Club','Diamond']
List_Rank = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
for x in range(len(List_Colour)):
    for y in range(len(List_Rank)):
        Deck.append(List_Colour[x]+' '+List_Rank[y])
# Init a Deck,avoid some unexpected bugs

class Player:
    # self.P_Card = []    ------------all player use the same cardpool list

    def __init__(self,Name):
        self.Name = Name
        self.P_Card = []        # for each player create a cardpool list

    def Add_Card(self,NewCard = "None 1"):
        
        if len(Deck) > 0:
            self.P_Card.append(NewCard)
        else:
            print("No More Card in Deck") 

    def Use_Card(self,Hand_Card_Number):
        Tmp_Card = self.P_Card [Hand_Card_Number - 1]
        self.P_Card.pop(Hand_Card_Number-1)
        return Tmp_Card
         
def Rebulid():
    for x in range(len(List_Colour)):
        for y in range(len(List_Rank)):
            Deck.append(List_Colour[x]+' '+List_Rank[y])

def Shuffle():
    import random
    random.shuffle(Deck)

def Pick():
    Tmp_card = Deck[0]
    Deck.pop(0)
    # print(Tmp_card)
    return Tmp_card

def Get_Point(ACard):
    Spilt_card = ACard.split(" ")
    match Spilt_card[1]:
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case _:
            return int(Spilt_card[1])

def Point_PK():
    # PVE POKE Point Pk Simple Game sample
    while True:
                Rebulid()
                Shuffle()
                Ex = input('Press any button for pick a card("e"/"E"for exit...)')
                if Ex == "E" or Ex == "e":
                    break
                Player_Pick =  Pick()
                AI_Pick =  Pick()
                print(f'You pick a {Player_Pick}')
                print(f'AI pick a {AI_Pick}')
                if Get_Point(Player_Pick) > Get_Point(AI_Pick):
                    print('You won!')
                elif Get_Point(Player_Pick) < Get_Point(AI_Pick):
                    print('You lose!')
                else:
                     print('H')
                print("==========================================")

def Function_Test():
    # Tunction tset
    Hand_Card = "None 0"
    while True:
        print('''=====================Function Select=====================
0.Check Deck and Hand Card
1.Rebulid
2.Shuffle
3.Pick
4.Get_Point(From Hand_Card)
              
e.Exit
              
''')
        Function_Select = input('Using function name')
        match Function_Select:
            case  '0':
                print(f'''Deck:{Deck}
Card_Sum:{len(Deck)}
Hand_Card:{Hand_Card}''')
            case  '1':
                Rebulid()
                Hand_Card = "None 0"
                print("Rebuild Over , please check new deck")
            case  '2':
                Shuffle()
                print("Shuffle Over , please check new deck")
            case  '3':
                Hand_Card = Pick()
                print(f"Hand_Card:{Hand_Card}")
            case  '4':
                print(Get_Point(Hand_Card))
            case "e" | "E":
                break

def CountAllCardPoint(Card_list = ["None 0"]):
    sum = 0
    for i in range(len(Card_list)):
        sum = sum + int(Get_Point(Card_list[i]))
    return sum
    
def PickOrNot(AllCardPoint,SafeTarget):
    if 21 - AllCardPoint >= SafeTarget:
        return True
    else:
        return False

def BlackJack():

    Human_Player = Player("Human_Player")
    AI_Player = Player("AI_Player")
    Human_Player.Name = input("Enter Your Name:")

    def WinOrNot():
        AIPoint = CountAllCardPoint(AI_Player.P_Card)
        HuPoint = CountAllCardPoint(Human_Player.P_Card)
        if AIPoint > HuPoint:
            if AIPoint <= 21:
                print('AI WIN')
                print('=====================================================')
            elif HuPoint <= 21:
                print('AI break,You win')
                print('=====================================================')
            else:
                print('Both break,no winner')
                print('=====================================================')
        elif AIPoint < HuPoint:           
            if HuPoint <= 21 :
                print('YOU WIN')
                print('=====================================================')
            elif AIPoint <= 21:
                print('YOU break,AI win')
                print('=====================================================')
            else:
                print('Both break,no winner')
                print('=====================================================')
        elif AIPoint == HuPoint:
            print('H')
            print('=====================================================')


    Rebulid()
    Shuffle()
    AI_SafeTarget =  random.randint(1,8)
    
    while True:
        dicission = input("Add Card or Over(A/O/E):")
        if dicission == "A" :

            Human_Player.Add_Card(Pick())
            print(f"{Human_Player.Name}'s Card:{Human_Player.P_Card}")

            if 21 - CountAllCardPoint(AI_Player.P_Card) > AI_SafeTarget:
                AI_Player.Add_Card(Pick())
                print(f"AI Card:{AI_Player.P_Card}")
            else:

                print("<AI Drop>")

        if dicission == "O" :
            print("<You Drop>")
            while  (21 - CountAllCardPoint(AI_Player.P_Card)) > AI_SafeTarget:
                #print(CountAllCardPoint(AI_Player.P_Card))  @for test
                AI_Player.Add_Card(Pick())
                print(f"AI Card:{AI_Player.P_Card}")
                print(f'{AI_Player.Name} Point: {CountAllCardPoint(AI_Player.P_Card)}')
                print('=====================================================')
            else:
                WinOrNot()
                break

        print(f'{Human_Player.Name} Point: {CountAllCardPoint(Human_Player.P_Card)}')       #print Human_Player Point
        print(f'{AI_Player.Name} Point: {CountAllCardPoint(AI_Player.P_Card)}')             #print AI Point
        print('=====================================================')

        if dicission == "E" :
            break

        
        




            
