class Student:

  def __init__(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_student(student_list):
 # sort the student in descending order of CGPA
  sorted_student =sorted(student_list,key=lambda student:student.cgpa,reverse=True)


 # syntax_lambda arg:exp
  return sorted_student


# Example usage:
student = [
   Student("Hari", "A123", 7.8),
   Student("Srikanth", "A124", 8.9),
   Student("saumya", "A125", 9.1),
   Student("Mahidhar", "A126", 9.9),
]

sorted_student = sort_student(student)

# print the sorted list of sudents
for student in sorted_student:
  print("Name: {},Roll Number: {},CGPA:". format(student.name,student.roll_number,student.cgpa))