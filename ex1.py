class Cercle():
    def __init__(self,rayon):
        self.__rayon = rayon

    def getRayon(self):
        return self.__rayon

    def __add__(self, other):
        if isinstance(other,Cercle) == True:
            return Cercle(self.__rayon + other.getRayon())
        else:
            return "Les des objets doivent être une instance de le classe Cercle"

    def __lt__(self, other):
        if isinstance(other,Cercle) == True:
            return self.__rayon < other.getRayon()
        else:
            return "Les des objets doivent être une instance de le classe Cercle"


    def __gt__(self, other):
        if isinstance(other,Cercle) == True:
            return self.__rayon > other.getRayon()
        else:
            return "Les des objets doivent être une instance de le classe Cercle"

    def __str__(self):
        return  "Le rayon est de " +str(self.getRayon())


#test programme
if __name__ == '__main__':
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
