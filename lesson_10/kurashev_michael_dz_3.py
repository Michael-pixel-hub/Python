class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = int(number_of_cells)
    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)
    def __str__(self):
        return f'{self.number_of_cells}'
    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            return 'Разность количества ячеек меньше нуля'
    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)
    def __truediv__(self, other):
        return Cell(self.number_of_cells / other.number_of_cells)
    def make_order(self, number_of_cells_in_a_row):
        if self.number_of_cells%number_of_cells_in_a_row == 0:
            a = int(self.number_of_cells/number_of_cells_in_a_row)
            b = number_of_cells_in_a_row * '*' + '\\n'
            summary_line = b * a
            return summary_line.rstrip('\\n')
        else:
            a = int(self.number_of_cells // number_of_cells_in_a_row)
            b = int(self.number_of_cells % number_of_cells_in_a_row)
            c = number_of_cells_in_a_row * '*' + '\\n'
            summary_line = (a * c)+ '*'* b
            return summary_line.rstrip('\\n')

a = Cell(12)
b = Cell(5)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.make_order(11))