class Complex():
    def __init__(self,reel, imag):
        self.__reel = reel
        self.__imag = imag

    def getReel(self):
        return self.__reel
    def getImag(self):
        return self.__imag

    def __add__(self, other):
        if isinstance(other,Complex)==True:
            return "addition : "+str(self.__reel + other.__reel)+ "+" +str(self.__imag + other.__imag)+"i"
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __sub__(self, other):
        if isinstance(other,Complex)==True:
            return "soustraction : " +str(self.__reel - other.__reel)+"+"+str(self.__imag - other.__imag)+"i"
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __mul__(self, other):
        if isinstance(other,Complex)==True:
            reel = self.__reel * other.__reel - self.__imag / other.__imag
            imag = self.__reel * other.__imag + self.__imag * other.__reel
            return "multiplication : "+str(reel)+" + "+str(imag)+"i"
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __truediv__(self, other):
        if isinstance(other,Complex)==True:
            reel = ((self.__reel * other.__reel) + (self.__imag * other.__imag)) / ((other.__reel**2)+(other.__imag**2))
            imag = ((self.__imag * other.__reel) - (self.__reel * other.__imag)) / ((other.__reel**2)+(other.__imag**2))
            return "division : "+str(reel)+ "+" +str(imag)+"i"
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __abs__(self):
        return "la valeur absolue : "+str(((self.__reel**2)+(self.__imag**2))**(1/2))

    def __eq__(self, other):
        if isinstance(other,Complex)==True:
            return self.__reel == other.__reel and self.__imag == other.__imag
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __ne__(self, other):
        if isinstance(other,Complex)== True:
            return self.__reel!= other.__reel or self.__imag != other.__imag
        else:
            return "Les objets doivent être une instance de le classe Cercle"

#test programme
if __name__ == '__main__':
    obj1 = Complex(2,3)
    obj2 = Complex(3,1)

    obj3 = obj1 + obj2
    obj4 = obj1 - obj2
    obj5 = obj1 * obj2
    obj6 = obj1 / obj2
    obj7 = abs(obj2)
    obj8 = obj1 == obj2
    obj9 = obj1 != obj2

    print(obj6)
