import numpy as np

def Create3DTable(x,y,z):
    mat = np.random.randint(0,10,size=[x,y,z])
    print(mat)
    print('Nombre de dimension:', mat.ndim)
    print('Shape de la matrice: ', mat.shape)
    print('Size de la matrice: ', mat.size)
    print('Dtype de la matrice: ', mat.dtype)
    print('Itemsize de la matrice: ', mat.itemsize)
    print('Data de la matrice: ', mat.data)
    return mat

def DeuxMatrices():
    mat1 = np.arange(9).reshape(3,3)
    mat2 = np.arange(2,11).reshape(3,3)
    mul = mat1 * mat2
    dot = np.dot(mat1,mat2)
    mat1T = mat1.transpose()
    print('Mat1 :')
    print(mat1)
    print('Mat2 :')
    print(mat2)
    print('Mat1 * Mat2 :')
    print(mul)
    print('Mat1 dot Mat2 :')
    print(mul)
    print('Transposer Mat1 :')
    print(mul)

def CalculerMatrice():
    mat = np.random.randint(0,10,size=[3,3])
    print('Matrice originale :')
    print(mat)
    det = np.linalg.det(mat)
    print('Determinant de la matrice : ', det)
    inv = np.linalg.inv(mat)
    print('Inverse de la matrice : ')
    print(inv)
    val, vec = np.linalg.eig(mat)
    print('valeurs :')
    print(val)
    print('vecteurs : ')
    print(vec)

if __name__=='__main__':
    #Create3DTable(4,3,2)
    #DeuxMatrices()
    CalculerMatrice()
