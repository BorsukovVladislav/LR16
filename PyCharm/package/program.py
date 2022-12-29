from package import help
from package import add
from package import out
from package import filter
from package import error


def main():
    """
    Главная функция
    """

    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'help':
            help.help_info()

        elif command == 'add':
            student = add.add_student()
            students.append(student)

            if len(students) > 1:
                students.sort(key=lambda item: item.get('group', ''))

        elif command == 'list':
            out.out_students(students)

        elif command == "filter list":
            filter_list = filter.students_filter(students)
            out.out_students(filter_list)

        else:
            error.err(command)
