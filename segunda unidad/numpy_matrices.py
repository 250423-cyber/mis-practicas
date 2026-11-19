import numpy as np
A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
suma=A+B
print("..SUMA(A+B)..")
print(suma)
prod_elem= A*B
print("..MULTIPLICACIÓN(A*B)..")
print(prod_elem)
prod_mat= A@B
print("..PRODUCTO MATRICIAL(A@B)..")
print(prod_mat)
transpuesta=A.T
print("..TRANSPUESTA DE A.T..")
print(transpuesta)
det=np.linalg.det(A)
inv=np.linalg.det(B)
print("..DETERMINADO DE A ..")
print(det)
print("..DETERMINADO DE B..")
print(inv)
