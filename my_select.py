from sqlalchemy import  func, desc, select, and_

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session
import logging


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    result = session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade),2).label('avg_grade')).\
        select_from(Grade).join(Student).group_by(Student.id)\
        .order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(discipline_id):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    result = session.query(
        Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).filter(Grade.discipline_id == discipline_id)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()
    return result


def select_3(discipline_id):
    """
    Знайти середній бал у групах з певного предмета.
    """
    result = session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    )\
        .select_from(Group)\
        .join(Student, Group.students)\
        .join(Grade, Student.grade)\
        .filter(Grade.discipline_id == discipline_id)\
        .group_by(Group.name)\
        .order_by(desc('avg_grade'))\
        .all()
    return result


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).all()
    return result

def select_5(teacher_id):
    """
    Знайти, які курси читає певний викладач.
    """
    result = session.query(Teacher.fullname, Discipline.name)\
        .select_from(Discipline)\
        .join(Teacher, Discipline.teacher)\
        .filter(Discipline.teacher_id == teacher_id)\
        .group_by(Teacher.fullname, Discipline.name)\
        .all()
    return result


def select_6(group_id):
    """
    Знайти список студентів у певній групі.
    """
    result = session.query(Group.name, Student.fullname)\
        .join(Group, Student.group)\
        .filter(Student.group_id == group_id)\
        .group_by(Group.name, Student.fullname)\
        .limit(10)\
        .all()
    return result


def select_7(group_id, discipline_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    result = session.query(Student.fullname, Group.name, Discipline.name, Grade.grade)\
        .join(Group, Student.group) \
        .join(Grade, (Student.id == Grade.student_id)) \
        .join(Discipline, (Grade.discipline_id == Discipline.id)) \
        .filter(Student.group_id == group_id) \
        .filter(Grade.discipline_id == discipline_id) \
        .limit(5)\
        .all()
    return result


def select_8(teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    result = session.query(Teacher.fullname, Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    )\
        .select_from(Teacher) \
        .join(Discipline, Teacher.id == Discipline.teacher_id) \
        .join(Grade, Discipline.id == Grade.discipline_id) \
        .filter(Discipline.teacher_id == teacher_id) \
        .group_by(Teacher.fullname, Discipline.name) \
        .all()
    return result


def select_9(student_id):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    result = session.query(Student.fullname, Discipline.name) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Discipline, Discipline.id == Grade.discipline_id) \
        .filter(Student.id == student_id) \
        .distinct() \
        .all()
    return result


def select_10(student_id, teacher_id):
    """
    Список дисциплін, які відвідує певний студент, та фамілія викладача.
    """
    result = session.query(Student.fullname, Discipline.name, Teacher.fullname) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Discipline, Discipline.id == Grade.discipline_id) \
        .join(Teacher, Discipline.teacher_id == Teacher.id) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .distinct() \
        .all()
    return result


def select_11(student_id, teacher_id):
    """
    Середній бал, який певний викладач ставить певному студентові.
    """
    result = session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade'),
        Teacher.fullname.label('teacher_name'),
        Student.fullname.label('student_name')
    ) \
        .join(Student, Grade.student_id == Student.id) \
        .join(Discipline, Grade.discipline_id == Discipline.id) \
        .join(Teacher, Discipline.teacher_id == Teacher.id) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Student.fullname) \
        .first()

    if result:
        return (result.avg_grade, result.teacher_name, result.student_name)
    else:
        return None


def select_12(discipline_id, group_id):
    """
    Оцінки студентів у певній групі з певного предмета на останньому занятті.
    """
    subquery = (select(Grade.date_of).join(Student).join(Group).where(
        and_(Grade.discipline_id == discipline_id, Group.id == group_id)
    ).order_by(desc(Grade.date_of)).limit(1).scalar_subquery())

    result = session.query(Discipline.name,
                      Student.fullname,
                      Group.name,
                      Grade.date_of,
                      Grade.grade
                      ) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group)\
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id, Grade.date_of == subquery)) \
        .order_by(desc(Grade.date_of)) \
        .all()
    return result



if __name__ == '__main__':
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    print(select_1())
    print(select_2(1))
    print(select_3(2))
    print(select_4())
    print(select_5(2))
    print(select_6(2))
    print(select_7(1, 1))
    print(select_8(1))
    print(select_9(1))
    print(select_10(3, 1))
    print(select_11(1, 1))
    print(select_12(1, 1))

