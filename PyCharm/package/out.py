def out_students(list_stud):
    """
    Вывод списка студентов
    """
    if list_stud:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 14,
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^14} |'.format(
                "№",
                "Ф.И.О.",
                "Номер группы",
            )
        )
        print(line)

        for idx, student in enumerate(list_stud, 1):
            print(
                '| {:>4} | {:<30} | {:<14} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                )
            )
        print(line)
    else:
        print("Список студентов пустой.")
