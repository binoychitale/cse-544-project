import scipy.stats


def perform_chi_square_test(matrix, alpha=0.05):
    row_totals = []
    col_totals = [0] * len(matrix[0])
    total = 0

    for row in matrix:
        row_sum = 0
        for (index, col) in enumerate(row):
            row_sum += col
            col_totals[index] += col
        row_totals.append(row_sum)
        total += row_sum

    f_obs = []
    f_exp = []
    for (row_index, row) in enumerate(matrix):
        for (col_index, col) in enumerate(row):
            expected = col_totals[col_index] * (row_totals[row_index] / total)
            print(expected)
            f_obs.append(col)
            f_exp.append(expected)
    # Note here that by default scipy takes dof to be k-1 where k is the number of cells.
    # We modify that behaviour to be consistent with that taught in class i.e (rows-1) * (cols-1)
    (chi_sq_statistic, p_value) = scipy.stats.chisquare(f_obs, f_exp,
                                                        (len(f_obs)-1) - (len(matrix) - 1) * (len(matrix[0]) - 1))
    if p_value < alpha:
        return p_value, False
    return p_value, True

print(perform_chi_square_test([[48, 54, 19], [7, 5, 4], [55, 50, 25]]))