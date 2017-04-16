import time
import example

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
        return self.a
    
    def solve(self, cell_i):
        if cell_i == self.cell_number - 1:
            return True
        cell = self.missed_cells[cell_i]
        i = cell[0]
        j = cell[1]
        candidates = self.get_candidate(i,j)
        for v in range(1, 10):
            if candidates[v]:
                self.a[i][j] = v    
                found = self.solve(cell_i+1)
                if found:
                    return found
        self.a[i][j] = 0
        return False
    
    def get_candidate(self, i, j):
        candidates = [True, True, True,True, True, True, True, True, True,True]
        for k in range(9):
            candidates[self.a[i][k]] = False
            candidates[self.a[k][j]] = False
        for i in range(3*(int(i/3)), 3*(int(i/3))+3):
            for j in range(3*(int(j/3)), 3*(int(j/3))+3):
                if self.a[i][j] != 0:
                    candidates[self.a[i][j]] = False
        return candidates
        
def main():
    
    from example import hard2
    
    sudoku = Sudoku(hard2)
    
    start = time.time()

    result = sudoku.run()
    
    end = time.time()

    print(end-start)
    print_result(result)

def print_result(result):
    for i in range(9):
        print(result[i])    

if __name__ == "__main__":
    main()