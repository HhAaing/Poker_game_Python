# from ctypes.wintypes import LPCOLORREF


class Card():

    RANK = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    COLOR = ['Club','Heart','Spade','Dimond']

    def __init__(self,rank,color) -> None:
        self.rank = rank 
        self.color = color

    #每一张牌确定一个序号
    def pic_order(self):
        #将rank对应数字值转化成int值
        if self.rank == 'J':
            Facenum = 11
        elif self.rank == 'Q':
            Facenum = 12
        elif self.rank == 'K':
            Facenum = 13
        else:
            Facenum = int(self.rank)
        #将color对应数字值转化成int值*13        
        if self.color == 'Club':
            Upcolor = 1
        elif self.color == 'Heart':
            Upcolor = 2
        elif self.color == 'Spade':
            Upcolor = 3
        elif self.color == 'Dimond':
            Upcolor = 4     
            return (Upcolor-1)*13 + Facenum
        
