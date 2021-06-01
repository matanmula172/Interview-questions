# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# convert string S to csv and find max value in column C
def convert_csv_to_matrix(s):
    arr = str(s).split('\n')
    mat = []
    for row in arr:
        mat.append(str(row).split(','))
    return mat


def get_col(C, mat):
    for i in range(len(mat)):
        if mat[0][i] == C:
            return i
    return


def get_arr(col_index, mat):
    arr = []
    for i in range(1, len(mat)):
        try:
            arr.append(int(mat[i][col_index]))
        except:
            pass
    return arr


def solution(S, C):
    mat = convert_csv_to_matrix(S)
    c_index = get_col(C, mat)
    arr = get_arr(c_index, mat)
    if len(arr) == 0:
        return
    return max(get_arr(c_index, mat))


S = "city,temp2,temp\nParis,10,.\nDubai,4,-4\nPorto,-1,-2"
C = "temp2"
# S = "id,name,age,act.,room,dep.\n1,Jack,68,T,13,8\n17,Betty,28,F,15,7"
# C = "age"
print(solution(S, C))
