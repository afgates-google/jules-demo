import unittest
from calculator import add, subtract, multiply, divide, sqrt, cube

class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_positive_negative(self):
        self.assertEqual(add(5, -3), 2)




    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_subtract_positive_negative(self):
        self.assertEqual(subtract(5,-3),8)



    def test_multiply_positive(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_positive_negative(self):
        self.assertEqual(multiply(5, -3), -15)



    def test_divide_positive(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        self.assertEqual(divide(6, 0), "Division by zero!")

    def test_divide_positive_negative(self):
        self.assertEqual(divide(6, -3), -2)





    def test_sqrt_positive(self):
        self.assertEqual(sqrt(4), 2)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_sqrt_negative(self):
        self.assertEqual(sqrt(-4), "Cannot calculate square root of a negative number")





    def test_cube_positive(self):
        self.assertEqual(cube(2), 8)

    def test_cube_negative(self):
        self.assertEqual(cube(-2), -8)

    def test_cube_zero(self):
        self.assertEqual(cube(0), 0)


if __name__ == '__main__':
    unittest.main()




