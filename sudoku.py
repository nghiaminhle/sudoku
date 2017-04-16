import time

class Sudoku:
    a = []
    missed_cells = []
    cell_number = 0

    def __init__(self, a):
        self.a = a
        for i in range(9):
            for j in range(9):
                if a[i][j] == 0:
                    self.missed_cells.append([i,j])

        self.cell_number = len(self.missed_cells)
    
    def run(self):
        self.solve(0)
    
    def solve(self, cell_i):
        cell = self.missed_cells[cell_i]
        i = cell[0]
        j = cell[1]
        for v in range(1,10):    
            if self.row_not_has_value(i, v) and self.col_not_has_value(j,v) and self.area_not_has_value(i,j,v):
                self.a[i][j] = v
                if cell_i < self.cell_number - 1:
                    self.solve(cell_i+1)
                else:
                    self.print_result()
        self.a[i][j] = 0

    def row_not_has_value(self, i, v):
        for j in range(9):
            if self.a[i][j] == v:
                return False
        return True

    def col_not_has_value(self, j, v):
        for i in range(9):
            if self.a[i][j] == v:
                return False
        return True

    def area_not_has_value(self, i, j, v):
        r = int(i/3)
        c = int(j/3)
        for i in range(3*r, 3*r+3):
            for j in range(3*c, 3*c+3):
                if self.a[i][j] == v:
                    return False
        return True

    def print_result(self):
        print("--------------")
        for i in range(9):
            print(self.a[i])


def main():
    a = [
        [0,0,5,0,9,0,0,0,1],
        [0,0,0,0,0,2,0,7,3],
        [7,6,0,0,0,8,2,0,0],
        [0,1,2,0,0,9,0,0,4],
        [0,0,0,2,0,3,0,0,0],
        [3,0,0,1,0,0,9,6,0],
        [0,0,1,9,0,0,0,5,8],
        [9,7,0,5,0,0,0,0,0],
        [5,0,0,0,3,0,7,0,0]
    ]

    sudoku = Sudoku(a)
    
    start = time.time()
    
    sudoku.run()
    
    end = time.time()

    print(end-start)

if __name__ == "__main__":
    main()