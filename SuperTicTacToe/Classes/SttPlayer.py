import random
from Classes.SttExceptions import InvalidInput


class SttPlayer(object):
    def __init__(self, owner):
        self.owner = owner
    def GetMove(self, ValidGrid = None) -> list[int]:
        pass

class ConsolePlayer(SttPlayer):
    def __init__(self, owner):
        self.owner = owner 
    def GetMove(self, ValidGrid = None) -> list[int]:
            command = input(f"{self.owner}'s Move {"(any grid)" if ValidGrid is None else f"(grid {ValidGrid})"} (grid, tile): ")
            try:
                return [int(i) for i in command.split(',')]
            except:
                raise InvalidInput

class EasyAIPlayer(SttPlayer):
    def __init__(self, owner, supergrid):
        self.owner = owner
        self.supergrid = supergrid
    def GetMove(self, ValidGrid = None) -> list[int]:
        validGrids = [ValidGrid] if ValidGrid is not None else [i for i in range(9) if self.supergrid.grids[i].IsUsable()]
        selectedGrid = random.choice(validGrids)
        validTiles = [i for i in range(9) if self.supergrid.grids[selectedGrid].tiles[i].owner == ' ']
        selectedTile = random.choice(validTiles)
        return [selectedGrid, selectedTile]
    
def GetPlayer(player: str, playerType: str, supergrid) -> SttPlayer:
    return ConsolePlayer(player) if playerType.lower()[0] == 'p' else EasyAIPlayer(player, supergrid)