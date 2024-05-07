from Classes.Tile import Tile


class Grid(object):
    def __init__(self):
        self.owner = " "
        self.tiles = [Tile() for i in range(9)]
        self.filled = False
    def IsUsable(self):
        return self.owner == ' ' and not self.filled
    def ClaimTile(self, player, tile):
        self.tiles[tile].owner = player
        if (self.tiles[0].owner != " " and self.tiles[0].owner == self.tiles[1].owner and self.tiles[0].owner == self.tiles[2].owner) or \
           (self.tiles[3].owner != " " and self.tiles[3].owner == self.tiles[4].owner and self.tiles[3].owner == self.tiles[5].owner) or \
           (self.tiles[6].owner != " " and self.tiles[6].owner == self.tiles[7].owner and self.tiles[6].owner == self.tiles[8].owner) or \
           (self.tiles[0].owner != " " and self.tiles[0].owner == self.tiles[3].owner and self.tiles[0].owner == self.tiles[6].owner) or \
           (self.tiles[1].owner != " " and self.tiles[1].owner == self.tiles[4].owner and self.tiles[1].owner == self.tiles[7].owner) or \
           (self.tiles[2].owner != " " and self.tiles[2].owner == self.tiles[5].owner and self.tiles[2].owner == self.tiles[8].owner) or \
           (self.tiles[0].owner != " " and self.tiles[0].owner == self.tiles[4].owner and self.tiles[0].owner == self.tiles[8].owner) or \
           (self.tiles[2].owner != " " and self.tiles[2].owner == self.tiles[4].owner and self.tiles[2].owner == self.tiles[6].owner):
            self.owner = player
        if all([t.owner != " " for t in self.tiles]):
            self.filled = True
    def __repr__(self):
        return f"{self.tiles[0]}|{self.tiles[1]}|{self.tiles[2]}\n" + \
                "-+-+-" + \
               f"{self.tiles[3]}|{self.tiles[4]}|{self.tiles[5]}\n" + \
                "-+-+-" + \
               f"{self.tiles[6]}|{self.tiles[7]}|{self.tiles[8]}\n"