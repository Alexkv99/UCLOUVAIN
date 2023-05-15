def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        templist = []
        for j in range(len(adj_mat)):
            if adj_mat[i][j] == 1:
                templist.append(j)
        adj_list.append(templist)
    return adj_list


adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
adj_list = mat_to_list(adj_mat)
