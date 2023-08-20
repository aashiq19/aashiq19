def print_matrix_list(matrix):
    for i in matrix:
        print(*i,sep=" ")
def convert_to_list(square_matrix_dict):
    lst=[]
    for i in square_matrix_dict:
        lst.append(square_matrix_dict[i])
    return lst
def convert_to_diagonal(matrix_dic):
    print("Non-diagonal matrix:")
    lst=convert_to_list(matrix_dic)
    print(f"In list of list format: {lst}")
    print("in original square format:")
    print_matrix_list(lst)
    print("================")
    print("Diagonal matrix:")
    for i in range(0,len(lst)):
        for j in range(0,len(lst[i])):
            if i!=j:
                lst[i][j]=0
    print(f"In list of list format: {lst}")
    print("in original square format:")
    print_matrix_list(lst)
square_matrix_dict = {1 : [1,2,3,4] , 2 : [4,5,6,7] , 3 : [7,8,9,3] , 4:[9,1,2,3] }
convert_to_diagonal(square_matrix_dict)
print()
print()
print()
square_matrix_dict = {1 : [1,2,3] , 2 : [4,5,6] , 3 : [7,8,9] }
convert_to_diagonal(square_matrix_dict)
