from matrix import Matrix

def test_determinant_1x1():
    matrix_1x1 = Matrix([[2.5]])
    assert matrix_1x1.determinant() == 2.5

def test_determinant_2x2():
    matrix_2x2 = Matrix([[2,3],[4,5]])
    assert matrix_2x2.determinant() == -2

def test_trace_1x1():
    matrix_1x1 = Matrix([[2.5]])
    assert matrix_1x1.trace() == 2.5

def test_trace_2x2():
    matrix_2x2 = Matrix([[2,3],[4,5]])
    assert matrix_2x2.trace() == 7

def test_inverse_1x1():
    matrix_1x1 = Matrix([[100]])
    assert matrix_1x1.inverse() == [[0.01]]

def test_inverse_2x2():
    matrix_2x2 = Matrix([[4,5],[7,1]])
    assert matrix_2x2.inverse() == [[-0.03225806451612903, 0.16129032258064516],
 [0.22580645161290322, -0.12903225806451613]]
    
def test_transpose_1x1():
    matrix_1x1 = Matrix([[5]])
    assert matrix_1x1.T() == [[0.5]]

def test_transpose_2x4():
    matrix_2x4 = Matrix([[5, 4, 1, 7], [2, 1, 3, 5]])
    assert matrix_2x4.T() == [[5, 2], [4, 1], [1, 3], [7, 5]]

def test_transpose_4x3():
    matrix_4x3 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
    assert matrix_4x3.T() == [[5, 7, 1, 8], [3, 1, 1, 9], [2, 4, 2, 1]]

def test_add():
    matrix_4x3_1 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
    matrix_4x3_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
    results = matrix_4x3_1 + matrix_4x3_2
    assert results == [[6, 4, 3], [8, 2, 5], [2, 2, 3], [9, 10, 2]]

def test_neg():
    matrix_4x3 = Matrix([[1, 0],
        [0, 1]])
    assert -matrix_4x3 == [[-1, 0],
        [0, -1]]

def test_sub():
    matrix_4x3_1 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
    matrix_4x3_2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
    results = matrix_4x3_1 - matrix_4x3_2
    assert results == [[4, 2, 1], [6, 0, 3], [0, 0, 1], [7, 8, 0]]

def test_mul():
    matrix_4x3_1 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
    matrix_4x3_2 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]])
    results = matrix_4x3_1 * matrix_4x3_2
    assert results == [[10, 6, 4], [14, 2, 8], [2, 2, 4], [16, 18, 2]]

def test_rmul():
    matrix_4x3_1 = Matrix([[5, 3, 2], [7, 1, 4], [1, 1, 2], [8, 9, 1]])
    assert 2 * matrix_4x3_1 == [[10, 6, 4], [14, 2, 8], [2, 2, 4], [16, 18, 2]]

if __name__ == "__main__":
    # Run the tests
    test_determinant_1x1()
    test_determinant_2x2()
    test_trace_1x1()
    test_trace_2x2()
    test_inverse_1x1()
    test_inverse_2x2()
    test_transpose_2x4()
    test_transpose_4x3()
    test_add()
    test_neg()
    test_sub()
    test_mul()
    test_rmul()

    print("All tests passed")