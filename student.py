from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


# Base.metadata.create_all(engine)

# student1 = Student(name='Lucas', age=30, grade='Fifth')
# student2 = Student(name='Igor', age=27, grade='Fifth')
# student3 = Student(name='Tales', age=30, grade='Fifth')
# student4 = Student(name='Andre', age=30, grade='Fifth')
# session.add(student1)

# session.add_all([student2, student3, student4])
# session.commit()


# Get all data
# students = session.query(Student)
# for student in students:
#     print(student.name, student.age, student.grade)


# Get data in order
# students = session.query(Student).order_by(Student.name)
# for student in students:
#     print(student.name)

# Get data by filtering
# student = session.query(Student).filter(Student.name == 'Tales').first()
# print(student.id)

# Get data with or
# students = session.query(Student).filter(
#     ((Student.name == 'Andre') | (Student.name == 'Igor')))

# for student in students:
#     print(student.name, student.age)

# Count the number of results
# student_count = session.query(Student).filter(
#     ((Student.name == 'Andre') | (Student.name == 'Igor'))).count()
# print(student_count)

# Update data
# student = session.query(Student).filter(Student.name == 'Lucas').first()
# student.name = 'Lucas Braga'
# session.commit()

# Delete data
# student = session.query(Student).filter(Student.name == 'Tales').first()
# session.delete(student)
# session.commit()
