# 3 задание
from sys import maxsize
import unittest

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_factorial_null(self):
        self.assertEqual(factorial(0), 1)
      
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_norm(self):
        self.assertEqual(factorial(4), 24)
        
    def test_factorial_minus(self):
        with self.assertRaisesRegex(ValueError, "Факториал отрицательного числа не определен"):
            factorial(-4)
    
    def test_factorial_big_number(self):
        with self.assertRaisesRegex(ValueError, "Факториал для 100 не поддерживается типом int"):
            factorial(100)
            
if __name__ == '__main__':
    unittest.main()