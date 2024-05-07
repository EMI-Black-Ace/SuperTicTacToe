from Classes.SuperGrid import SuperGrid
from Classes.InvalidMove import *

print("Welcome to Super Tic Tac Toe!")
game = SuperGrid()
while not game.gameOver:
    print(game)
    command = input(f"{game.player.OwnerTurn}'s Move (grid, tile): ")
    try:
        action = [int(i) for i in command.split(',')]
        game.player.ClaimTile(action[0], action[1])
    except InvalidMove:
        print("Invalid move.\n" + \
              "The tile the previous player selected corresponds to which grid you must make your move in, unless you cannot make a move in that grid.\n" + \
              "In such a case, you can select a move in any grid.\n" + \
              "A move cannot be to an occupied space or a won or completed subgrid.")
        continue
    except:
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