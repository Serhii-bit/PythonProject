# ##################### ДЗ 14.1. Виняток користувача
#
# class GroupLimitExceededError(Exception):
#     """Виняток, що виникає при спробі додати більше 10 студентів до групи."""
#
#     def __init__(self, message="Не можна додати більше 10 студентів до групи"):
#         self.message = message
#         super().__init__(self.message)
#
#
# class Group:
#
#     def __init__(self, number):
#         self.number = number
#         self.group = set()
#
#     def add_student(self, student):
#         if len(self.group) >= 10:
#             raise GroupLimitExceededError("Не можна додати більше 10 студентів до групи")
#         self.group.add(student)
#
#     def delete_student(self, last_name):
#         student_to_remove = self.find_student(last_name)
#         if student_to_remove:
#             self.group.remove(student_to_remove)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#         return None
#
#     def __str__(self):
#         all_students = '\n'.join([str(student) for student in self.group])
#         return f'Група: {self.number}\n{all_students}'
#
#
# class Student:
#     def __init__(self, gender, age, first_name, last_name, record_book):
#         self.gender = gender
#         self.age = age
#         self.first_name = first_name
#         self.last_name = last_name
#         self.record_book = record_book
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}, {self.age} років'
#
#
# try:
#     st1 = Student('Male', 20, 'Steve', 'Jobs', 'AN142')
#     st2 = Student('Female', 22, 'Liza', 'Taylor', 'AN145')
#     gr = Group('PD1')
#
#     for i in range(11):
#         gr.add_student(Student('Male', 20 + i, f'Name{i}', f'Surname{i}', f'AN14{i + 1}'))
#
# except GroupLimitExceededError as e:
#     print(f"Помилка: {e}")
#
# print(gr)
#
# ##################### ДЗ 14.2. Створення власних модулів