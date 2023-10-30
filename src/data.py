from src.models import Teacher, Group, Student, Discipline, Grade
import argparse

parser = argparse.ArgumentParser(description='School Management CLI')
parser.add_argument('-a', '--action', help='Command: create, list, delete, remove, update')

parser.add_argument('-m', '--model', help='Model: Student, Teacher, Group, Discipline, Grade' )
parser.add_argument('-fn', '--fullname', help='Full name of the user')
parser.add_argument('-n', '--name', help='Name of the user')
parser.add_argument('-g', '--grade', help='Grade value')
parser.add_argument('-d', '--date_of', help='Date of the record')
parser.add_argument('-idt', '--teacher_id', help='ID of the teacher')
parser.add_argument('-idg', '--group_id', help='ID of the group')
parser.add_argument('-ids', '--student_id', help='ID of the student')
parser.add_argument('-idd', '--discipline_id', help='ID of the discipline')
parser.add_argument('-l', '--login', help='Login of the user')
parser.add_argument('-id', '--id')



arguments = parser.parse_args()

my_arg = vars(arguments)

action = my_arg.get('action')
fullname = my_arg.get('fullname')
name = my_arg.get('name')
grade = my_arg.get('grade')
date_of = my_arg.get('date_of')
teacher_id = my_arg.get('teacher_id')
group_id = my_arg.get('group_id')
student_id = my_arg.get('student_id')
login = my_arg.get('login')
discipline_id = my_arg.get('discipline_id')
model = my_arg.get('model')
_id = my_arg.get('id')


arguments = parser.parse_args()


model_map = {
            'create': {
                'Teacher': (Teacher, {'fullname': fullname}),
                'Group': (Group, {'name': name}),
                'Student': (Student, {'fullname': fullname, 'group_id': group_id}),
                'Discipline': (Discipline, {'name': name, 'teacher_id': teacher_id}),
                'Grade': (Grade, {'grade': grade, 'date_of': date_of, 'student_id': student_id, 'discipline_id': discipline_id})
            },
            'list': {
                'Teacher': (Teacher, {}),
                'Group': (Group, {}),
                'Student': (Student, {}),
                'Discipline': (Discipline, {}),
                'Grade': (Grade, {})
            },
            'update': {
                'Teacher': (Teacher, {}),
                'Group': (Group, {}),
                'Student': (Student, {}),
                'Discipline': (Discipline, {}),
                'Grade': (Grade, {})
            },
            'remove': {
                'Teacher': (Teacher, {}),
                'Group': (Group, {}),
                'Student': (Student, {}),
                'Discipline': (Discipline, {}),
                'Grade': (Grade, {})
            }
            }
