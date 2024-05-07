from Classes.InvalidMove import InvalidMove


class PlayerMove(object):
    OwnerTurn = 'X'
    ValidGrid = None
    def __init__(self, supergrid):
        self.supergrid = supergrid
    def ClaimTile(self, grid, tile):
        if self.ValidGrid is not None and grid != self.ValidGrid:
            raise InvalidMove()
        if not self.supergrid.grids[grid].IsUsable() or self.supergrid.grids[grid].tiles[tile].owner != ' ':
            raise InvalidMove()
        self.supergrid.SetTileOwner(self.OwnerTurn, grid, tile)
        self.OwnerTurn = 'O' if self.OwnerTurn == 'X' else 'X'
        self.ValidGrid = tile if self.supergrid.grids[tile].IsUsable() else None