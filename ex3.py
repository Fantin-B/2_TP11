class Rational():
    def __init__(self, numerateur, denominateur):
        self.__numerateur = numerateur
        self.__denominateur = denominateur

    def getNum(self):
        return self.__numerateur
    def getDenom(self):
        return self.__denominateur


    def pgcd(self,a,b):
        if b == 0 :
            return "erreur"

        reste = a % b
        while reste != 0 :
            a = b
            b = reste
            reste = a % b
        return b

    def ppcm(self,a,b):
        pgcd = self.pgcd(a,b)
        ppcm = (a*b) / pgcd
        return ppcm

    def simplify(self,a,b):
        pgcd = self.pgcd(a, b)
        a = a/pgcd
        b = b/pgcd
        return a,b



    def __add__(self, other):
        if isinstance(other,Rational) == True :
            ppcm_B_D = self.ppcm(self.__denominateur,other.__denominateur)
            partieNum1 = self.__numerateur * (ppcm_B_D/self.__denominateur)
            partieNum2 = other.__numerateur * (ppcm_B_D/other.__denominateur)
            final = self.simplify(partieNum1+partieNum2,ppcm_B_D)
            if final[1]==1:
                return "résultat :"+str(int(final[0]))
            else:
                return "résultat :"+str(int(final[0]))+"/"+str(int(final[1]))
        else:
            return "Les objets doivent être une instance de le classe Cercle"
    def __sub__(self, other):
        if isinstance(other,Rational) == True :
            ppcm_B_D = self.ppcm(self.__denominateur,other.__denominateur)
            partieNum1 = self.__numerateur * (ppcm_B_D/self.__denominateur)
            partieNum2 = other.__numerateur * (ppcm_B_D/other.__denominateur)
            final = self.simplify(partieNum1-partieNum2,ppcm_B_D)
            if final[1]==1:
                return "résultat :"+str(int(final[0]))
            else:
                return "résultat :"+str(int(final[0]))+"/"+str(int(final[1]))
        else:
            return "Les objets doivent être une instance de le classe Cercle"


    def __mul__(self, other):
        if isinstance(other,Rational) == True :
            num = self.__numerateur*other.__numerateur
            denom = self.__denominateur*other.__denominateur
            final = self.simplify(num,denom)
            if final[1]==1:
                return "résultat :"+str(int(final[0]))
            else:
                return "résultat :"+str(int(final[0]))+"/"+str(int(final[1]))
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __truediv__(self, other):
        if isinstance(other,Rational) == True :
            num = self.__numerateur * other.__denominateur
            denom = self.__denominateur * other.__numerateur
            final = self.simplify(num,denom)
            if final[1]==1:
                return "résultat :"+str(int(final[0]))
            else:
                return "résultat :"+str(int(final[0]))+"/"+str(int(final[1]))
        else:
            return "Les objets doivent être une instance de le classe Cercle"


    def __eq__(self, other):
        if isinstance(other,Rational) == True :
            fraction1 = self.simplify(self.__numerateur,self.__denominateur)
            fraction2 = self.simplify(other.__numerateur,other.__denominateur)
            if fraction1[0]==fraction2[0] and fraction1[1]==fraction2[1]:
                return "Les deux équations sont égales"
            else:
                return "Les deux équation ne sont pas égales"
        else:
            return "Les objets doivent être une instance de le classe Cercle"

    def __ne__(self, other):
        if isinstance(other,Rational) == True :
            fraction1 = self.simplify(self.__numerateur,self.__denominateur)
            fraction2 = self.simplify(other.__numerateur,other.__denominateur)
            if fraction1[0]!=fraction2[0] or fraction1[1]!=fraction2[1]:
                return "Les deux équations ne sont pas égales"
            else:
                return "Les deux équation sont égales"
        else:
            return "Les objets doivent être une instance de le classe Cercle"


#test prgogramme
if __name__=='__main__':
    obj1 = Rational(6,3)
    obj2 = Rational(3,2)

    obj3 = obj1 + obj2
    obj4 = obj1 - obj2
    obj5 = obj1 * obj2
    obj6 = obj1 / obj2
    print(obj5)
