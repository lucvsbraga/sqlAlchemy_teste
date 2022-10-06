from session import Banco
from student import Student

banco = Banco()

student = banco.session.query(Student).filter(
    Student.name == 'Lucas Braga').first()
print(student.grade)
