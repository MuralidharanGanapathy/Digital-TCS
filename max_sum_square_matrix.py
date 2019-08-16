n = 4
matrix = [[2,-8,4,-6],[7,1,-5,3],[-9,7,6,5],[8,3,2,-4]]
sum_list = []
#matrix dimensions
for l in range(2,n + 1):
    #row_selector
    for i in range(n - l + 1):
        #col_selector
        for j in range(0, n - l + 1):
            temp_sum = 0
            #element retrieval
            for k in range(i, i + l):
                temp_sum += sum(matrix[k][j: j + l])
            sum_list.append(temp_sum)
print(max(sum_list))
