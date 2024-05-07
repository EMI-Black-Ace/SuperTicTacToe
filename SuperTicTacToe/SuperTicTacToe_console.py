from Classes.SttExceptions import *
from Classes.SuperGrid import SuperGrid

print("Welcome to Super Tic Tac Toe!")
xplayer = input("Who's playing X? (player, CPU): ")
oplayer = input("Who's playing O? (player, CPU): ")
game = SuperGrid(xplayer, oplayer)
while not game.gameOver:
    print(game)
    try:
        game.player.ClaimTile()
    except InvalidMove:
        print("Invalid move.\n" + \
              "The tile the previous player selected corresponds to which grid you must make your move in, unless you cannot make a move in that grid.\n" + \
              "In such a case, you can select a move in any grid.\n" + \
              "A move cannot be to an occupied space or a won or completed subgrid.")
        continue
    except Exception as ex:
        print(ex)
        confirmQuit = input("Do you want to quit? y/n: ")
        if confirmQuit.lower()[0] == 'y':
            print("Maybe next time we'll finish?")
            break
        else:
            continue
else:
    print("Ooh, looks like a stalemate." if game.winner is None else f"{game.winner} Wins!")
    print("Great game!")
    exit()
print("Thanks for playing.")