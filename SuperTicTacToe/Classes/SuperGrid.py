from Classes.Grid import Grid
from Classes.PlayerMove import PlayerMove
from Classes.SttPlayer import ConsolePlayer, EasyAIPlayer, GetPlayer


class SuperGrid(object):
    
    def __init__(self, xplayer, oplayer):
        self.player = PlayerMove(self, GetPlayer('X', xplayer, self), GetPlayer('O', oplayer, self))
        self.winner = None
        self.gameOver = False
        self.grids = [Grid() for i in range(9)]
    def SetTileOwner(self, owner, grid, tile):
        self.grids[grid].ClaimTile(owner, tile)
        if (self.grids[0].owner != ' ' and self.grids[0].owner == self.grids[1].owner and self.grids[0].owner == self.grids[2].owner) or \
           (self.grids[3].owner != ' ' and self.grids[3].owner == self.grids[4].owner and self.grids[3].owner == self.grids[5].owner) or \
           (self.grids[6].owner != ' ' and self.grids[6].owner == self.grids[7].owner and self.grids[6].owner == self.grids[8].owner) or \
           (self.grids[0].owner != ' ' and self.grids[0].owner == self.grids[3].owner and self.grids[0].owner == self.grids[6].owner) or \
           (self.grids[1].owner != ' ' and self.grids[1].owner == self.grids[4].owner and self.grids[1].owner == self.grids[7].owner) or \
           (self.grids[2].owner != ' ' and self.grids[2].owner == self.grids[5].owner and self.grids[2].owner == self.grids[8].owner) or \
           (self.grids[0].owner != ' ' and self.grids[0].owner == self.grids[4].owner and self.grids[0].owner == self.grids[8].owner) or \
           (self.grids[2].owner != ' ' and self.grids[2].owner == self.grids[4].owner and self.grids[2].owner == self.grids[6].owner):
            self.winner = owner
            self.gameOver = True
        elif all(not g.IsUsable() for g in self.grids):
            self.gameOver = True
    def __repr__(self):
        return f"{self.grids[0].tiles[0]}|{self.grids[0].tiles[1]}|{self.grids[0].tiles[2]} || {self.grids[1].tiles[0]}|{self.grids[1].tiles[1]}|{self.grids[1].tiles[2]} || {self.grids[2].tiles[0]}|{self.grids[2].tiles[1]}|{self.grids[2].tiles[2]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[0].tiles[3]}|{self.grids[0].tiles[4]}|{self.grids[0].tiles[5]} || {self.grids[1].tiles[3]}|{self.grids[1].tiles[4]}|{self.grids[1].tiles[5]} || {self.grids[2].tiles[3]}|{self.grids[2].tiles[4]}|{self.grids[2].tiles[5]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[0].tiles[6]}|{self.grids[0].tiles[7]}|{self.grids[0].tiles[8]} || {self.grids[1].tiles[6]}|{self.grids[1].tiles[7]}|{self.grids[1].tiles[8]} || {self.grids[2].tiles[6]}|{self.grids[2].tiles[7]}|{self.grids[2].tiles[8]}\n" + \
                "======##=======##======\n" + \
               f"{self.grids[3].tiles[0]}|{self.grids[3].tiles[1]}|{self.grids[3].tiles[2]} || {self.grids[4].tiles[0]}|{self.grids[4].tiles[1]}|{self.grids[4].tiles[2]} || {self.grids[5].tiles[0]}|{self.grids[5].tiles[1]}|{self.grids[5].tiles[2]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[3].tiles[3]}|{self.grids[3].tiles[4]}|{self.grids[3].tiles[5]} || {self.grids[4].tiles[3]}|{self.grids[4].tiles[4]}|{self.grids[4].tiles[5]} || {self.grids[5].tiles[3]}|{self.grids[5].tiles[4]}|{self.grids[5].tiles[5]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[3].tiles[6]}|{self.grids[3].tiles[7]}|{self.grids[3].tiles[8]} || {self.grids[4].tiles[6]}|{self.grids[4].tiles[7]}|{self.grids[4].tiles[8]} || {self.grids[5].tiles[6]}|{self.grids[5].tiles[7]}|{self.grids[5].tiles[8]}\n" + \
                "======##=======##======\n" + \
               f"{self.grids[6].tiles[0]}|{self.grids[6].tiles[1]}|{self.grids[6].tiles[2]} || {self.grids[7].tiles[0]}|{self.grids[7].tiles[1]}|{self.grids[7].tiles[2]} || {self.grids[8].tiles[0]}|{self.grids[8].tiles[1]}|{self.grids[8].tiles[2]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[6].tiles[3]}|{self.grids[6].tiles[4]}|{self.grids[6].tiles[5]} || {self.grids[7].tiles[3]}|{self.grids[7].tiles[4]}|{self.grids[7].tiles[5]} || {self.grids[8].tiles[3]}|{self.grids[8].tiles[4]}|{self.grids[8].tiles[5]}\n" + \
                "-+-+- || -+-+- || -+-+-\n" + \
               f"{self.grids[6].tiles[6]}|{self.grids[6].tiles[7]}|{self.grids[6].tiles[8]} || {self.grids[7].tiles[6]}|{self.grids[7].tiles[7]}|{self.grids[7].tiles[8]} || {self.grids[8].tiles[6]}|{self.grids[8].tiles[7]}|{self.grids[8].tiles[8]}\n"