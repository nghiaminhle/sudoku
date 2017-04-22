import time

class Sudoku:
    missed_cells = []
    cell_number = 0
    count = 0

    def __init__(self, a):
        self.a = a
        for i in range(9):
            for j in range(9):
                if a[i][j] == 0:
                    self.missed_cells.append([i, j])

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
            found = self.solve(cell_i + 1)
            if found:
                return found
        self.a[i][j] = 0
        return False

    def get_candidate(self, i, j):
        candidates = [True, True, True, True, True, True, True, True, True, True]
        for k in range(9):
            candidates[self.a[i][k]] = False
            candidates[self.a[k][j]] = False
            candidates[self.a[3*int(i/3) + int(k/3)][3*int(j/3) + k%3]] = False

        candidates = [k for k, v in enumerate(candidates) if v]
        return candidates

    def get_best_cell(self, cell_i):
        if cell_i > self.cell_number - 1:
            return None, []
        best_candidates = []
        best_cell_idx = -1
        best_candidates_count = 10
        for idx, cell in enumerate(self.missed_cells):
            if idx < cell_i:
                continue
            i = cell[0]
            j = cell[1]
            candidates = self.get_candidate(i, j)
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

    print_result(super_hard)
    print("----------------")
    sudoku = Sudoku(super_hard)

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
