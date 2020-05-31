class Matrix:

    def __init__(self, matrix_string):
        self.matrix = []
        # Converting the input strings into Matrix
        self.matrix = [list(map(int, i.split())) for i in matrix_string.strip().split('\n')]
        '''for i in matrix_string.strip().split("\n"):
            self.matrix.append(list(map(int, i.split())))'''

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        self.col = []
        for i in range(len(self.matrix)):
            self.col.append(self.matrix[i][index-1])
        return self.col

'''matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
print(matrix.row(2))'''