import time

class Sudoku:
    missed_cells = []
    cell_number = 0
    cell_candidate_number = []
    count = 0
    rows = []
    cols = []
    areas = []

    def __init__(self, a):
        self.a = a
        self.rows = [0 for x in range(9)]
        self.cols = [0 for x in range(9)]
        self.areas = [0 for x in range(9)]

        for i in range(9):
            for j in range(9):
                if a[i][j] == 0:
                    self.missed_cells.append([i, j])
                else:
                    bits = 1<<a[i][j]
                    self.rows[i] = self.rows[i] | bits
                    self.cols[j] = self.cols[j] | bits
                    self.areas[3*int(i/3)+int(j/3)] = self.areas[3*int(i/3)+int(j/3)] | bits

        self.cell_number = len(self.missed_cells)
        self.best_candidate_threshold = 1

    def run(self):
        self.count = 0
        self.solve(0)
        return self.a

    def solve(self, cell_i):
        self.count += 1
        if cell_i > self.cell_number - 1:
            return True
        candidates = self.get_best_cell(cell_i)
        cell = self.missed_cells[cell_i]
        i = cell[0]
        j = cell[1]
        for v in candidates:
            self.a[i][j] = v

            bits = 1<<v
            
            self.rows[i] = self.rows[i] | bits
            self.cols[j] = self.cols[j] | bits
            self.areas[3*int(i/3)+int(j/3)] = self.areas[3*int(i/3)+int(j/3)] | bits
            
            if self.solve(cell_i + 1):
                return True

            bits = ~bits
            self.rows[i] = self.rows[i] & bits
            self.cols[j] = self.cols[j] & bits
            self.areas[3*int(i/3)+int(j/3)] = self.areas[3*int(i/3)+int(j/3)] & bits

        self.a[i][j] = 0
        return False

    def get_best_cell(self, cell_i):
        if cell_i > self.cell_number - 1:
            return None, []
        best_candidates = []
        best_cell_idx = -1
        best_candidates_count = 10
        #for idx, cell in enumerate(self.missed_cells):
        for idx in range(cell_i, self.cell_number):
            cell = self.missed_cells[idx]
            i = cell[0]
            j = cell[1]
            candidates = []
            candidates_count = 0
            
            for k in range(1,10):
                bits = 1<<k
                if (not self.rows[i] & bits) and (not self.cols[j] & bits) and (not self.areas[3*int(i/3)+int(j/3)] & bits):
                    candidates.append(k)
            candidates_count = len(candidates)
            if candidates_count <= best_candidates_count:
                best_candidates = candidates
                best_cell_idx = idx
                best_candidates_count = candidates_count
                if candidates_count <= self.best_candidate_threshold:
                    break

        tmp = self.missed_cells[cell_i]
        self.missed_cells[cell_i] = self.missed_cells[best_cell_idx]
        self.missed_cells[best_cell_idx] = tmp
        return best_candidates

def main():
    from example import hard1
    from example import hard2
    from example import easy
    from example import super_hard
    from example import norvig1
    from example import norvig2
    from example import norvig3

    a = super_hard

    print_result(a)
    print("----------------")
    sudoku = Sudoku(a)

    start = time.clock()

    result = sudoku.run()

    end = time.clock()

    print(end-start, sudoku.count)
    print_result(result)

def print_result(result):
    for i in range(9):
        print(result[i])

if __name__ == "__main__":
    main()