# class Employee:
#     def __init__(self, first_name, last_name, office, title):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.office = office
#         self.title = title

#     def _get_full_name(self):
#         full_name = f"{self.last_name}, {self.first_name}"
#         return full_name

#     def is_southwest(self):
#         if self.office in ['las vegas', 'scottsdale', 'austin']:
#             return True
#         else:
#             return False

#     def get_employee_description(self):
#         full_name = self.get_full_name()

#         description = f'{full_name}: {self.title}: {self.office}: Southwest: {self.is_southwest()}'
#         return description

# dan = Employee(
#     first_name='Dan',
#     last_name='Leonard',
#     office='Scottsdale',
#     title='Analyst'
# )

# full_name = dan.get_full_name()

# print(full_name)

# is_southwest = dan.is_southwest()