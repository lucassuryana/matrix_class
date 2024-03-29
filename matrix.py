import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def transpose(matrix):
    matrix_transpose = []
    num_rows = len(matrix[:])
    num_columns = len(matrix[0])
    for i in range(0,num_columns):
        rows = []
        for j in range(0,num_rows):
            rows.append(matrix[j][i])
        matrix_transpose.append(rows)
            
    
    return matrix_transpose

def dot_product(vector_one, vector_two):
    
    product = []
    
    for i in range(0,len(vector_one)):
        sum_point = vector_one[i] * vector_two[i]
        product.append(sum_point)
    
    results = sum(product)
    
    return results

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            det = self.g[0][0]
        else:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            det = (a * d) - (b * c)

        return det


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trc = 0
        if len(self.g) == 1:
            trc = self.g[0][0]
        else:
            for i in range(0,len(self.g[0])):
                trc += self.g[i][i]
        
        return trc

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inv = []
        if len(self.g) == 1:
            value = [1 / self.g[0][0]]
            inv.append(value)
        else:
            det = self.determinant()
            val_0_0 = self.g[1][1] / det
            val_0_1 = -self.g[0][1] / det
            val_1_0 = -self.g[1][0] / det
            val_1_1 = self[0][0] / det

            inv = [[val_0_0, val_0_1],[val_1_0, val_1_1]]
                
        return Matrix(inv)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        transpose = []
        num_rows = len(self.g)
        num_columns = len(self.g[0])
        for i in range(0,num_columns):
            rows = []
            for j in range(0, num_rows):
                rows.append(self.g[j][i])
            transpose.append(rows)

        return Matrix(transpose)

        # TODO - your code here

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #

        added_state = []
        num_rows = len(self.g)
        num_columns = len(self.g[0])
        for i in range(0, num_rows):
            rows = []
            for j in range(0, num_columns):
                val = self.g[i][j] + other[i][j]
                rows.append(val)
            added_state.append(rows)
        
        return Matrix(added_state)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        new_val = []
        num_rows = len(self.g)
        num_columns = len(self.g[0])
        for i in range(0, num_rows):
            rows = []
            for j in range(0, num_columns):
                val = -self.g[i][j]
                rows.append(val)
            new_val.append(rows)
        
        return Matrix(new_val)       

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        neg_state = []
        num_rows = len(self.g)
        num_columns = len(self.g[0])
        for i in range(0, num_rows):
            rows = []
            for j in range(0, num_columns):
                val = self.g[i][j] - other[i][j]
                rows.append(val)
            neg_state.append(rows)
        
        return Matrix(neg_state)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        product = []
        
        transpose_matrixB = transpose(other)
        num_rows_A = len(self.g)
        num_rows_B = len(transpose_matrixB)
        
        for i in range(num_rows_A):
            row = []
            for j in range(num_rows_B):
                dot_result = dot_product(self.g[i], transpose_matrixB[j])
                row.append(dot_result)
            product.append(row)
        
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            rmul_state = []
            num_rows = len(self.g)
            num_columns = len(self.g[0])
            for i in range(0, num_rows):
                rows = []
                for j in range(0, num_columns):
                    val = self.g[i][j] * other
                    rows.append(val)
                rmul_state.append(rows)
            
            return Matrix(rmul_state)     
                