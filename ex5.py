import numpy as np

class Matrice():
    def __init__(self, data):
        self.__data = data

    def __str__(self):
        matrice = np.array([[self.__data[0],self.__data[1]],
                            [self.__data[2],self.__data[3]]])
        return "matrice\n" +str(matrice)

    def __add__(self, other):
        if isinstance(other,Matrice) == True :
            newData = [self.__data[0]+other.__data[0],self.__data[1]+other.__data[1],self.__data[2]+other.__data[2],self.__data[3]+other.__data[3]]
            newMatrice = Matrice(newData)
            return newMatrice

    def __iadd__(self, other):
        if isinstance(other,Matrice) == True :
            self.__data[0] += other.__data[0]
            self.__data[1] += other.__data[1]
            self.__data[2] += other.__data[2]
            self.__data[3] += other.__data[3]
            return Matrice(self.__data)

    def __sub__(self, other):
        if isinstance(other,Matrice) == True :
            newData = [self.__data[0]-other.__data[0],self.__data[1]-other.__data[1],self.__data[2]-other.__data[2],self.__data[3]-other.__data[3]]
            newMatrice = Matrice(newData)
            return newMatrice

    def __isub__(self, other):
        if isinstance(other,Matrice) == True :
            self.__data[0] -= other.__data[0]
            self.__data[1] -= other.__data[1]
            self.__data[2] -= other.__data[2]
            self.__data[3] -= other.__data[3]
            return Matrice(self.__data)

#testProgramme
if __name__=='__main__':
    mat1 = Matrice([0,1,2,3])
    mat2 = Matrice([1,1,1,1])

    mat3 = mat1 + mat2
    #mat1 += mat2
    mat4 = mat1 - mat2
    #mat1 -= mat2
    print(mat1)
