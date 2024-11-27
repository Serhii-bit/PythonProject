###############  ДЗ 13.1. Група студентів
#
# class Human:
#     def __init__(self, gender, age, first_name, last_name):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"
#
# class Student(Human):
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         super().__init__(gender, age, first_name, last_name)
#         self.record_book = record_book
#
#     def __str__(self):
#         return f"{super().__str__()}, Record Book: {self.record_book}"
#
# class Group:
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         self.group.add(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def delete_student(self, last_name):
#         student = self.find_student(last_name)
#         if student:
#             self.group.remove(student)
#
#     def __str__(self):
#         all_students = "\n".join(str(student) for student in self.group)
#         return f"Group Number: {self.number}\n{all_students}"
#
#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
#
# gr = Group('PD1')
#
# gr.add_student(st1)
# gr.add_student(st2)
#
# print(gr)
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
#
# gr.delete_student('Taylor')
# print(gr)
#
# gr.delete_student('Taylor')


###############  ДЗ 13.2. Клас "Цифровий лічильник"


# class DigitalCounter:
#     def __init__(self, current=0, min_value=0, max_value=10):
#         # Ініціалізація атрибутів
#         self.current = current
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def set_max(self, max_max):
#         """Встановлення максимального значення лічильника"""
#         self.max_value = max_max
#
#     def set_min(self, min_min):
#         """Встановлення мінімального значення лічильника"""
#         self.min_value = min_min
#
#     def set_current(self, start):
#         """Встановлення початкового значення лічильника"""
#         self.current = start
#
#     def step_up(self):
#         """Збільшуємо лічильник на 1. Якщо досягнуто максимуму - викидаємо помилку"""
#         if self.current >= self.max_value:
#             raise ValueError("Максимум")
#         self.current += 1
#
#     def step_down(self):
#         """Зменшуємо лічильник на 1. Якщо досягнуто мінімуму - викидаємо помилку"""
#         if self.current <= self.min_value:
#             raise ValueError("Мінімум")
#         self.current -= 1
#
#     def get_current(self):
#         """Повертаємо поточне значення лічильника"""
#         return self.current
#
# counter = DigitalCounter()
# counter.set_current(5)
# counter.step_up()
# counter.step_up()
#
# print(counter.get_current())
#
# counter.set_max(10)
# counter.set_min(0)
# counter.step_up()
# counter.step_up()
# counter.step_up()
#
#
# try:
#     counter.step_up()
# except ValueError as e:
#     print(e)
#
# counter.step_down()
# counter.step_down()
#
# try:
#     counter.step_down()
# except ValueError as e:
#     print(e)
#
# print(counter.get_current())
