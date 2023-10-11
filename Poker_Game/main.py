import Deck

while True:
    Select_Game = input('''=====================Game Select=====================
1.Point PK   
2.Blackjack 
test.Function Test

''')
    
# Match Menu to Choice Game
    match Select_Game :
        case "1" | "Point PK":
            Deck.Point_PK()
        case "2" | "Blackjack ":
            Deck.BlackJack()          
        case "test":
            Deck.Function_Test()
        case _:
            print("Error input")