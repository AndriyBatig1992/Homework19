from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, event, Date
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25), unique=True)
    password = Column(String(25))

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship(User)


@event.listens_for(Teacher, 'before_update')
def update_updated_at(maper, conn, target):
    target.updated_at = func.now()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship(User)

@event.listens_for(Group, 'before_update')
def update_updated_at(maper, conn, target):
    target.updated_at = func.now()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship('Group', backref='students')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship(User)

@event.listens_for(Student, 'before_update')
def update_updated_at(maper, conn, target):
    target.updated_at = func.now()

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    teacher = relationship('Teacher', backref='disciplines')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship(User)

@event.listens_for(Discipline, 'before_update')
def update_updated_at(maper, conn, target):
    target.updated_at = func.now()

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    date_of = Column('date_of', Date, nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    discipline_id = Column('discipline_id', ForeignKey('disciplines.id', ondelete='CASCADE'))
    student = relationship('Student', backref='grade')
    discipline = relationship('Discipline', backref='grade')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    user = relationship(User)

@event.listens_for(Grade, 'before_update')
def update_updated_at(maper, conn, target):
    target.updated_at = func.now()



