# System of Linear Equations
# x + 2y = 8
# 5x - 3y = 1

# Gauss Jordan Method
# [1 2]  [x] = [8]
# [5 -3] [y] = [1]

import numpy as np
A=np.array([[1,2,-7],  #First Row
            [5,-3,7],# Second Row
            [3,-6,9]])# Third Row
B=np.array([[7,8,-3],
            [4,7,2]
            ,[5,6,1]])
mat_sum=A+B


print(A)
print("------------------------")
print(B)
print("------------------------")
print(mat_sum)
print("------------------------")
print(np.add(A,B))
print("------------------------")
# Matrix Scaler Multiplication
A=2*A
print(A)
print("------------------------")
# Matrix Vector Multiplication
C=np.array([[-1],[5],[-7]])
D=A@C # Dot Product
print(D)
print("------------------------")
print(np.dot(A.T,C))
print("------------------------")

# Matrix Matrix Multiplication
print(A@B)
print("------------------------")
# Inverse of a Matrix
print(np.linalg.inv(A))
print("------------------------")
I=np.linalg.inv(A)@A
print(np.round(I))
print("------------------------")
# Matrix Transpose
print(A.T)
print("------------------------")
#Solving Linear Equation Using Gauss Jordan Method
# x-3y+6z=21
# 3x+2y-5z=-30
# 2x-5y+2z=-6
A=np.array([[1,-3,6],[3,2,-5],[2,-5,2]])
A_inv=np.linalg.inv(A)
B=np.array([[21],[-30],[-6]])
Sol=A_inv@B
print(Sol)
print("------------------------")

# GAussian Elemination Methods
# Rules:
#     1. Addition and Subtraction of Two equation.
#     2. Multiplication of an equation by a number.
# x+3y+5z=-1
# 2x+2y-z=1
# x+3y+2z=2
# R[x,y,z]=S
R=np.array([[1,3,5],[2,2,-1],[1,3,2]])
S=np.array([[-1],[1],[2]])
t=np.linalg.solve(R,S)
print(t)
print("------------------------")
# A set of n linearly independent column vectors with n elements forms a basis

# Eigen Values & Eigen Vector
a=np.array([[4,2],[1,3]])
w,v=np.linalg.eig(a)
print("E value: ",w)# w stores Eigen Values
print("E vector: ",v)# v stores Eigen Vector5


    