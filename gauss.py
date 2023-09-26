# Author: DerVogel101
# Github: https://github.com/DerVogel101
# Date: 26.09.2023
# Description: This is a Gauss algorithm that solves a system of linear equations for my Flutter app.

from copy import deepcopy
import re


class Gauss:
    class SolveError(Exception):
        pass

    class SizeError(Exception):
        pass

    class FormatError(Exception):
        pass

    def __init__(self, matrix: list[list[float | int]]):
        """
        The matrix must be in the following format:\n
        [[a, b, c, solution],\n
        [d, e, f, solution],\n
        [g, h, i, solution]]
        :raises Gauss.SizeError: If the matrix is too big
        :param matrix: Matrix to solve
        """
        # set variables
        self.__matrix = matrix
        self.__matrix = self.__matrix_convert_float()  # convert matrix to float
        self.__matrix_len = len(self.__matrix)  # get matrix length

        self.__validate_matrix()  # validate matrix format

        # check if matrix is in the right dimension and set variables: x, y, z, a, b, c, ...
        variables = {0: "x", 1: "y", 2: "z"}
        if self.__matrix_len <= 3:
            pass
        elif self.__matrix_len <= 26:
            for i in range(self.__matrix_len - 3):
                variables[i + 3] = chr(i + 97)
        else:
            raise Gauss.SizeError("Matrix zu groß")
        self.__variables = variables

    def __matrix_convert_float(self) -> list[list[float]]:
        """
        Converts the matrix to float
        :return: Converted matrix
        """
        for a, i0 in enumerate(self.__matrix):
            for b, i1 in enumerate(i0):
                self.__matrix[a][b] = float(i1)
        return deepcopy(self.__matrix)

    def __validate_matrix(self) -> None:
        """
        Validates the matrix format
        :raises Gauss.FormatError: If the matrix is not valid
        """
        for line in self.__matrix:
            if len(line) != self.__matrix_len + 1:
                raise Gauss.FormatError("Matrix nicht gültig")

    def gauss_solve(self) -> list[list[float]]:
        """
        Solves the matrix with the Gauss algorithm
        :raises Gauss.SolveError: If the matrix is not solvable
        :return: Solved matrix
        """
        try:
            # iterate over matrix
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
                        # If no line was found, the matrix is not solvable
                        raise Gauss.SolveError("Matrix nicht lösbar")
                # iterate over line
                for edit_index, edit_line in enumerate(self.__matrix):
                    # Check if line is not pivot line
                    if not edit_index == top_index:
                        # make temp deepcopy
                        temp = deepcopy(self.__matrix[edit_index][top_index] / self.__matrix[top_index][top_index])
                        # iterate over line
                        for lpos, lpos_val in enumerate(edit_line):
                            # edit line and subtract and do math
                            self.__matrix[edit_index][lpos] -= temp * self.__matrix[top_index][lpos]
        except ZeroDivisionError:
            raise Gauss.SolveError("Matrix nicht lösbar")
        return deepcopy(self.__matrix)

    def move_line(self, line, target) -> None:
        """
        Moves a line to another position
        :param line: The line to move
        :param target: The target position
        """
        self.__matrix.insert(target, self.__matrix.pop(line))

    def gauss_solve_result(self) -> list[list[float]]:
        """
        Makes the solution of the matrix more readable
        :return: Solution of the matrix
        """
        for index in range(self.__matrix_len):
            # divide line by pivot element
            temp_div = deepcopy(self.__matrix[index][index])
            for col_index in range(self.__matrix_len + 1):
                self.__matrix[index][col_index] /= temp_div
        return deepcopy(self.__matrix)

    def print_result(self) -> None:
        """
        Prints the result of the matrix
        """
        print("Lösung:")
        for index, line in enumerate(self.__matrix):
            print(f"{self.__variables[index]} = {line[-1]}")

    def get_result(self) -> dict[str, float]:
        """
        Returns the result of the matrix
        :return: Result of the matrix
        """
        result = {}
        for index, line in enumerate(self.__matrix):
            result[self.__variables[index]] = line[-1]
        return result


def list_to_matrix(matrix_list: list[str]) -> list[list[float]]:
    """
    converts a list of lines to a matrix
    :param matrix_list: input list like ["2+3=1", "4-1=11"]
    :return: output matrix like [[2, 3, 1], [4, -1, 11]]
    """
    output_matrix = []
    matrix_str_list = deepcopy(matrix_list)
    # convert matrix_str_list to float
    for line in matrix_str_list:
        line = line.split("=")  # split line at "="
        # get multiplier and solution using regex
        multiplier = re.findall(r'([+-]?\d+\.?\d*)', line[0])
        multiplier = [float(m) for m in multiplier]  # convert multiplier to float
        solution = float(line[1])  # convert solution to float

        output_matrix.append(multiplier + [solution])  # add multiplier and solution to output_matrix

    return output_matrix


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
                     [48, 8, 1, 0, 0]],
                 6: [[1.0, 1.0, 1.0, 1.0, 1.0],
                     [-1.0, 1.0, -1.0, 1.0, -1.0],
                     [3.0, -2.0, 1.0, 0.0, 0.0],
                     [3.0, 2.0, 1.0, -0.0, 0.0]]
                 }
    matrix = beispiele[6]
    gauss = Gauss(matrix)
    gauss.gauss_solve()
    gauss.gauss_solve_result()
    print(gauss.get_result())
    gauss.print_result()
