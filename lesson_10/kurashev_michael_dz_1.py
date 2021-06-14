class Matrix:
    def __init__(self, list_lists):
        self.matrix1 = list_lists
    def matrix_creation(self):
        summary_line = ''
        for ind_line in self.matrix1:
            if not summary_line:
                for ind in ind_line:
                    summary_line = summary_line + str(ind) + ' '
            else:
                summary_line = summary_line + '\n'
                for ind in ind_line:
                    summary_line = summary_line + str(ind) + ' '
        summary_line = summary_line + '\n'
        return summary_line

a = Matrix([[2, 3], [4, 2], [2, 2], [5, 6, 8]])
b = Matrix([[2, 3], [4, 2], [2, 2]])
print(a.matrix_creation())
print(b.matrix_creation())