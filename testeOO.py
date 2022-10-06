from session import Banco
from student import Student

banco = Banco()
# engine = create_engine(
#     "mysql+pymysql://root:Senha2mysql.@localhost:3306/bigbox", echo=False)

# Session = sessionmaker(bind=engine)
# session = Session()

student3 = Student(name='Tales', age=30, grade='Fifth')
# session.add(student3)
# session.commit()

student = banco.session.query(Student).filter(
    Student.name == 'Lucas Braga').first()
print(student.grade)
