import numpy as np
import pandas as pd

from session import Banco
from student import Student

banco = Banco()

student = banco.session.query(Student).filter(
    Student.name == 'Syllas').first()

if not student:
    print('não foi encontrado')
print(student.name)

df = pd.DataFrame(data=[['Lívia', 22, 'Nineth'], ['Jane', 25, 'Third'], [
                  'Jordana', 28, 'PHD']], columns=['name', 'age', 'grade'])


def adicionar(df):
    newStudent = Student(name=df[0], age=df[1], grade=df[2])
    banco.session.add(newStudent)

    # print(df[0])


df.apply(lambda x: adicionar(x), axis=1)
banco.session.commit()
