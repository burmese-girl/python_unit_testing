import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, 5), 6)
        self.assertEqual(calc.add(1, 19), 20)
        self.assertEqual(calc.add(10, 15), 25)

    def test_sub(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(30, 15), 15)
        self.assertEqual(calc.subtract(20, 10), 10)
        self.assertEqual(calc.subtract(10, 3), 7)

    def test_multipy(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, 5), 5)
        self.assertEqual(calc.multiply(3, 5), 15)
        self.assertEqual(calc.multiply(1, 6), 6)


def test_divide(self):
    self.assertEqual(calc.divide(10, 5), 2)
    self.assertEqual(calc.divide(15, 5), 3)
    self.assertEqual(calc.divide(25, 5), 5)
    self.assertEqual(calc.divide(20, 4), 5)

    with self.assertRaise(ValueError):
        calc.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
