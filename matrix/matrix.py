class Matrix:

    def __init__(self, matrix_string):
        self.matrix = []
        # Converting the input strings into Matrix
        self.matrix = [list(map(int, i.split())) for i in matrix_string.strip().split('\n')]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        self.col = []
        for i in range(len(self.matrix)):
            self.col.append(self.matrix[i][index-1])
        return self.col