class Duree():
    def __init__(self, heure, minute, seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde

    def setMinute(self, newMinute):
        self.__minute = newMinute
    def setSeconde(self, newSeconde):
        self.__seconde = newSeconde

    def __str__(self):
        if self.__seconde >= 60 :
            newSeconde = self.__seconde - 60
            newMinute = self.__minute + 1
            self.setSeconde(newSeconde)
            self.setMinute(newMinute)
        return str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+"s"

    def __add__(self, other):
        if isinstance(other,Duree) == True :
            seconde = self.__seconde + other.__seconde
            if seconde >= 60 :
                minute = 1
                seconde = seconde-60
            else:
                minute = 0
            minute += self.__minute + other.__minute
            if minute >= 60 :
                heure = 1
                minute = minute-60
            else:
                heure = 0
            heure += self.__heure + other.__heure

            return Duree(heure,minute,seconde)




#TestProgramme
if __name__=='__main__':
    obj1 = Duree(1,40,40)
    obj2 = Duree(2,19,20)

    obj3 = obj1 + obj2
    print(obj3)
