# Init a Deck,avoid some unexpected bugs
Deck = []
List_Colour = ['Spade','Heart','Club','Diamond']
List_Rank = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
for x in range(len(List_Colour)):
    for y in range(len(List_Rank)):
         Deck.append(List_Colour[x]+' '+List_Rank[y])
    
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




            
