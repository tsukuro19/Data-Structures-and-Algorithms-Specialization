import sys

matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

def get_cost(matrix,matrix_list):
    cost=0
    for x in range(3):
        for y in range(3):
            cost+=abs(matrix_list[x][y]-matrix[x][y])
    return cost


def Magic_Square(matrix):
    min_matrix=sys.maxsize
    for ref in matrix_list:
        cost=get_cost(matrix,ref)
        min_matrix=min(cost,min_matrix)
    return min_matrix


if __name__=="__main__":
    matrix=[]
    for i in range(3):
        row=[int(row_temp) for row_temp in input().strip().split(' ')]
        matrix.append(row)
    print(Magic_Square(matrix))