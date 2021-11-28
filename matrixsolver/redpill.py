
def transpose2x2 (my_mat):
    '''
    Transposes a 2x2 matrix.

    Args:
        my_mat(nested list)

    Returns:
        my_mat_t (nested list)
    '''
    my_mat_row1 = []
    my_mat_row2 = []

    my_mat_row1.append(my_mat[0][0])
    my_mat_row1.append(my_mat[1][0])
        
    my_mat_row2.append(my_mat[0][1])
    my_mat_row2.append(my_mat[1][1])

    my_mat_t = [my_mat_row1, my_mat_row2]
    return (my_mat_t)
#####

def det2x2 (my_mat):
    '''
    Finds the determinant of a 2x2 matrix.

    Agrs:
        my_mat(nested list)

    Returns:
        det_my_mat(nested list)
    
    '''

    #ad - bc
    return ((my_mat[0][0] * my_mat[1][1]) - (my_mat[0][1] * my_mat[1][0]))
#####


bigboi = [[1,2],[3,4]]
print(transpose2x2(bigboi))
print(det2x2(bigboi))
