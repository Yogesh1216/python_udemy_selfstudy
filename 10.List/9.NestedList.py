l1 = [10,20,['a','b',['c','d']],30,40]
print(l1)

print(l1[2][2][0])  # c

# adding matrix
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C=[]
for i in range(len(A)):
    sum=[]
    for j in range(len(B)):
        sum.append(A[i][j]+B[i][j])
    C.append(sum)
print(C)



