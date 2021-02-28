#Coded by: Tirtharaj Dash
#Website: htps://tirtharajdash.github.io

import numpy as np

#input the matrix dim (square matrix: n \times n)
#remember that Python is 0-indexed: [0:n-1]\times[0:n-1]
n = int(input('Enter size of your A matrix:'))

#construct A''
A_dd = np.zeros([n,n])

#diagonal case
for i in range(0,n):
    A_dd[i,i] = -6

#two end points on main diagonal
A_dd[0,1] = 1
A_dd[n-1,n-2] = 1

#for 2nd row to n-1th row
for i in range(1,n-1):
    A_dd[i,i-1] = 1
    A_dd[i,i+1] = 1

print('A\'\'')
print(A_dd)

#identity of size n \times n
I = np.eye(n)

#Construct A'
A_dash = np.zeros([n**2,n**2])

count = 0
for i in range(0,n):
    A_dash[i*n:(i+1)*n,i*n:(i+1)*n] = A_dd

    count = count + 1
    #place the I matrix on up and down diagonal
    #there will always be n-1 I matrix on up and down diagnoals
    if count <= n-1:
        A_dash[i*n:(i+1)*n,(i+1)*n:(i+2)*n] = I
        A_dash[(i+1)*n:(i+2)*n,i*n:(i+1)*n] = I

print('A\'')
print(A_dash)

#Construct A
m = n**2;
A = np.zeros([m**2,m**2])
I = np.eye(m)

count = 0
for i in range(0,m):
    A[i*m:(i+1)*m,i*m:(i+1)*m] = A_dash
    
    count = count + 1
    #place the I matrix on up and down diagonal
    if count <= m-1:
        A[i*m:(i+1)*m,(i+1)*m:(i+2)*m] = I
        A[(i+1)*m:(i+2)*m,i*m:(i+1)*m] = I

print('A')
print(A)


#save the matrices to files
A_ddash = np.matrix(A_dd)
with open('A_ddash.txt','wb') as f:
    for line in A_ddash:
        np.savetxt(f, line, fmt='%.0f')

A_dash = np.matrix(A_dash)
with open('A_dash.txt','wb') as f:
    for line in A_dash:
        np.savetxt(f, line, fmt='%.0f')

A = np.matrix(A)
with open('A.txt','wb') as f:
    for line in A:
        np.savetxt(f, line, fmt='%.0f')
