def students_filter(list_s):
    """
    Вывод списка студентов со средним баллом больше 4
    """
    if len(list_s) > 0:
        filter_s = []
        for student in list_s:
            if sum(student.get('marks')) / 5 > 4:
                filter_s.append(student)
        return filter_s
    else:
        print("Список студентов пустой.")