
def transpose2x2 (my_mat):
    '''
    Transposes a 2x2 matrix.

    Args:
        my_mat(list)

    Returns:
        my_mat_t (list)
    '''
    my_mat_row1 = []

    my_mat_row1.append(bigboi[0][0])
    my_mat_row1.append(bigboi[1][0])
        
    my_mat_row2 =[]

    my_mat_row2.append(bigboi[0][1])
    my_mat_row2.append(bigboi[1][1])

    my_mat_t = [my_mat_row1, my_mat_row2]
    print (my_mat_t)

bigboi = [[1,2],[3,4]]
transpose2x2(bigboi)



