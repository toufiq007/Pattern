#  Nested list
print_A = [[" " for i in range(5)] for j in range(7)]
print_M = [[" " for i in range(5)] for j in range(7)]
print_U = [[" " for i in range(5)] for j in range(7)]
print_R = [[" " for i in range(5)] for j in range(7)]
print_B = [[" " for i in range(5)] for j in range(7)]
print_K = [[" " for i in range(5)] for j in range(7)]
print_E = [[" " for i in range(5)] for j in range(7)]
print_I = [[" " for i in range(5)] for j in range(7)]
print_D = [[" " for i in range(5)] for j in range(7)]


# Printing Letter Shape

#  A shape
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or row==2 or (row==0 and (col!=0 and col!=4)):
            print_A[row][col] = "*"


#  M shape
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (col==row and row < 3) or (row+col==4 and row<3):
            print_M[row][col] = "*"


#  U shape
for row in range(6):
    for col in range(5):
        if ((col==0 or col==4) and row!=5) or (row==5 and (col!=0 and col!=4)):
            print_U[row][col] = "*"


# B shape
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and (col>0 and col<4)):
            print_R[row][col] = "*"


# R shape
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
            print_B[row][col] = "*"


# K shape
for row in range(7):
    for col in range(5):
        if (col==0 or (col==1 and row==3 ) or ((col==2) and (row==2 or row==4)) or ((col==3 and (row==1 or row==5))) or ((col==4) and (row==0  or row==6))):
           print_K[row][col] = "*"



# E shape
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3 or row== 6) and (col>0)):
           print_E[row][col] = "*"


# I shape
for row in range(7):
    for col in range(5):
        if col==2 or ((row==0 or row==6) and (col!=2)):
           print_I[row][col] = "*"

# D shape
for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print_D[row][col] = "*"


print()


# combine EID letter

for i in range(7):
    for j in range(5):
        print(print_E[i][j],end=' ')
    print(end='   ')
    for j in range(5):
        print(print_I[i][j],end=' ')
    print(end='   ')
    
    for j in range(5):
        print(print_D[i][j],end=' ')
        print(end=' ')
    
    print()


print()
print()


# combine MUBARAK letter

for i in range(7):        
    for j in range(5):
        print(print_M[i][j],end=' ')
    print(end='     ')
    
    for j in range(5):
        print(print_U[i][j],end=' ')
    print(end='     ')

    for j in range(5):
        print(print_B[i][j],end=' ')
    print(end='     ')

    for j in range(5):
        print(print_A[i][j],end=' ')
    print(end='     ')
    
    for j in range(5):
        print(print_R[i][j],end=' ')
    print(end='     ')
    
    for j in range(5):
        print(print_A[i][j],end=' ')
    print(end='     ')
    for j in range(5):
        print(print_K[i][j],end=' ')
    print(end='     ')
    
    print()
