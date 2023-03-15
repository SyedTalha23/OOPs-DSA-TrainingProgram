mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]%2!=0:
            mat[i][j]=mat[i][j]**2
        else:          
            mat[i][j]=mat[i][j]**3
print(mat)

#list comprehension version below
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat=[[mat[i][j]**2 if mat[i][j]%2!=0 else mat[i][j]**3 for j in range(len(mat[i]))]for i in range(len(mat))] #elif doesnt work in list comprehension
print(mat)




