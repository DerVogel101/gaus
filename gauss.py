from copy import deepcopy


class Gauss:
    class SolveError(Exception):
        pass

    class MatrixError(Exception):
        pass

    def __init__(self, matrix):
        self.__matrix = matrix
        self.__matrix = self.__matrix_convert_float()
        self.__matrix_len = len(self.__matrix)

        self.__validate_matrix()

        variables = {0: "x", 1: "y", 2: "z"}
        if self.__matrix_len <= 3:
            pass
        elif self.__matrix_len <= 26:
            for i in range(self.__matrix_len - 3):
                variables[i + 3] = chr(i + 97)
        else:
            raise Gauss.MatrixError("Matrix zu groß")
        self.__variables = variables

    def __matrix_convert_float(self):
        for a, i0 in enumerate(self.__matrix):
            for b, i1 in enumerate(i0):
                self.__matrix[a][b] = float(i1)
        return deepcopy(self.__matrix)

    def __validate_matrix(self):
        for line in self.__matrix:
            if len(line) != self.__matrix_len + 1:
                raise Gauss.MatrixError("Matrix nicht gültig")

    def gauss_solve(self):
        try:
            for top_index, matrix_line in enumerate(self.__matrix):
                # Check if pivot element is zero
                if self.__matrix[top_index][top_index] == 0:
                    # Find a line to swap
                    for swap_index in range(top_index + 1, len(self.__matrix)):
                        if self.__matrix[swap_index][top_index] != 0:
                            # Swap lines
                            self.move_line(swap_index, top_index)
                            break
                    else:
                        raise Gauss.SolveError("Matrix nicht lösbar")
                for edit_index, edit_line in enumerate(self.__matrix):
                    if not edit_index == top_index:
                        temp = deepcopy(self.__matrix[edit_index][top_index] / self.__matrix[top_index][top_index])
                        for lpos, lpos_val in enumerate(edit_line):
                            self.__matrix[edit_index][lpos] -= temp * self.__matrix[top_index][lpos]
        except ZeroDivisionError:
            raise Gauss.SolveError("Matrix nicht lösbar")
        return deepcopy(self.__matrix)

    def move_line(self, line, target) -> None:
        self.__matrix.insert(target, self.__matrix.pop(line))

    def gauss_solve_result(self):
        for index in range(self.__matrix_len):
            temp_div = deepcopy(self.__matrix[index][index])
            for col_index in range(self.__matrix_len + 1):
                self.__matrix[index][col_index] /= temp_div
        return deepcopy(self.__matrix)

    def print_result(self):
        print("Lösung:")
        for index, line in enumerate(self.__matrix):
            print(f"{self.__variables[index]} = {line[-1]}")

    def get_result(self):
        result = {}
        for index, line in enumerate(self.__matrix):
            result[self.__variables[index]] = line[-1]
        return result


if __name__ == '__main__':
    beispiele = {1: [[2, 3, 1, 1],
                     [4, -1, 3, 11],
                     [3, 1, -1, 0]],

                 2: [[2, 3, 0, 1, 1],
                     [4, -1, 0, 1, 1],
                     [2, 2, 1, -1, -1],
                     [1, 3, 2, 2, 0]],

                 3: [[1, -1, 1, 0],
                     [0.25, 0.5, 1, -2.25],
                     [1, 1, 0, 0]],

                 4: [[0, 0, 0, 1, 1],
                     [1, 1, 1, 1, 2],
                     [0, 2, 0, 0, 0],
                     [3, 2, 1, 0, 0]],

                 5: [[8, 4, 2, 1, 4],
                     [64, 16, 4, 1, 2],
                     [12, 4, 1, 0, 0],
                     [48, 8, 1, 0, 0]]
                 }
    matrix = beispiele[5]
    gauss = Gauss(matrix)
    gauss.gauss_solve()
    gauss.gauss_solve_result()
    print(gauss.get_result())
    gauss.print_result()
