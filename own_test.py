from matrix import Matrix

def test_determinant_1x1():
    matrix_1x1 = Matrix([[2.5]])
    assert matrix_1x1.determinant() == 2.5

def test_determinant_2x2():
    matrix_2x2 = Matrix([[2,3],[4,5]])
    assert matrix_2x2.determinant() == -2

if __name__ == "__main__":
    # Run the tests
    test_determinant_1x1()
    test_determinant_2x2()

    print("All tests passed")