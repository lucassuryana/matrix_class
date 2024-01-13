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

if __name__ == "__main__":
    # Run the tests
    test_determinant_1x1()
    test_determinant_2x2()
    test_trace_1x1()
    test_trace_2x2()
    test_inverse_1x1()
    test_determinant_2x2()

    print("All tests passed")