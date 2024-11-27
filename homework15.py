
############### ДЗ 15.1. Клас «Прямокутник

# import math
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         """Площа прямокутника"""
#         return self.width * self.height
#
#     def __eq__(self, other):
#         """Порівняння прямокутників за площею"""
#         if isinstance(other, Rectangle):
#             return self.get_area() == other.get_area()
#         return False
#
#     def __add__(self, other):
#         """Додавання двох прямокутників (сума площ)"""
#         if isinstance(other, Rectangle):
#             total_area = self.get_area() + other.get_area()
#             side_length = math.sqrt(total_area)
#             return Rectangle(side_length, side_length)
#
#     def __mul__(self, n):
#         """Множення прямокутника на число n (площа збільшується в n разів)"""
#         if isinstance(n, (int, float)):
#             total_area = self.get_area() * n
#             side_length = math.sqrt(total_area)
#             return Rectangle(side_length, side_length)
#         return NotImplemented
#
#     def __str__(self):
#         """Створення строкового представлення прямокутника"""
#         return f"Rectangle(width={self.width}, height={self.height})"
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# r3 = r1 + r2
# assert math.isclose(r3.get_area(), 26), 'Test2'
#
# r4 = r1 * 4
# assert math.isclose(r4.get_area(), 32), 'Test3'
#
# print(r3)
# print(r4)


#########################  ДЗ 15.2. Клас «Правильний дріб»

# import math
#
# class Fraction:
#     def __init__(self, a, b):
#         if b == 0:
#             raise ValueError("Знаменник не може бути нульовим.")
#         self.a = a
#         self.b = b
#         self.simplify()
#
#     def simplify(self):
#         """Метод для спрощення дробу до найменших чисел"""
#         gcd = math.gcd(self.a, self.b)
#         self.a //= gcd
#         self.b //= gcd
#
#     def __mul__(self, other):
#         """Множення дробів"""
#         if isinstance(other, Fraction):
#             num = self.a * other.a
#             den = self.b * other.b
#             return Fraction(num, den)
#         return NotImplemented
#
#     def __add__(self, other):
#         """Додавання дробів"""
#         if isinstance(other, Fraction):
#             num = self.a * other.b + self.b * other.a
#             den = self.b * other.b
#             result = Fraction(num, den)
#             result.simplify()
#             return result
#         return NotImplemented
#
#     def __sub__(self, other):
#         """Віднімання дробів"""
#         if isinstance(other, Fraction):
#             num = self.a * other.b - self.b * other.a
#             den = self.b * other.b
#             result = Fraction(num, den)
#             result.simplify()
#             return result
#         return NotImplemented
#
#     def __eq__(self, other):
#         """Перевірка на рівність дробів"""
#         if isinstance(other, Fraction):
#             return self.a == other.a and self.b == other.b
#         return NotImplemented
#
#     def __gt__(self, other):
#         """Перевірка на більше"""
#         if isinstance(other, Fraction):
#             return self.a * other.b > self.b * other.a
#         return NotImplemented
#
#     def __lt__(self, other):
#         """Перевірка на менше"""
#         if isinstance(other, Fraction):
#             return self.a * other.b < self.b * other.a
#         return NotImplemented
#
#     def __str__(self):
#         """Рядкове представлення дробу"""
#         return f"Fraction: {self.a}, {self.b}"
#
#
# f_a = Fraction(2, 3)
# f_b = Fraction(3, 6)
# f_c = f_b + f_a
# assert str(f_c) == 'Fraction: 7, 6', f"Expected 'Fraction: 7, 6' but got {str(f_c)}"  # Оновлений результат
#
# f_d = f_b * f_a
# assert str(f_d) == 'Fraction: 1, 3', f"Expected 'Fraction: 1, 3' but got {str(f_d)}"
#
# f_e = f_a - f_b
# assert str(f_e) == 'Fraction: 1, 6', f"Expected 'Fraction: 1, 6' but got {str(f_e)}"
#
# assert f_d < f_c
# assert f_d > f_e
# assert f_a != f_b
#
# f_1 = Fraction(2, 4)
# f_2 = Fraction(3, 6)
# assert f_1 == f_2
#
# print('OK')

