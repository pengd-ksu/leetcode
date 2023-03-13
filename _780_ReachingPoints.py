class Solution:
    def reachingPoints_brute(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        #Can't finish on large numbers
        if sx == tx and sy == ty:
            return True
        elif sx > tx or sy > ty:
            return False
        return self.reachingPoints(sx+sy, sy, tx, ty) or self.reachingPoints(sx, sy+sx, tx, ty)
    
    def reachingPoints_2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if sx == tx:
                return (ty - sy) % sx == 0
            elif sy == ty:
                return (tx - sx) % sy == 0
            elif ty > tx:
                ty %= tx#last step, smaller gets there first. Suppose ty > tx
                #ty=ty-tx will get to ty on last step, modulo tx on both sides
            else:
                tx %= ty
        return False