def shape(A):
    rows = len(A)
    columns = len(A[0]) if A else 0
    return rows, columns


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [x[j] for x in A]


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]
