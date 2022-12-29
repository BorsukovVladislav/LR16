def add_student():
    """
    Добавление студента в список
    """
    name = input("Фамилия и инициалы студента: ")
    group = int(input("Номер группы: "))
    marks = list(map(int, input("Пять оценок студента: ").split()))

    if len(marks) != 5:
        print("Неверное количество оценок")
        return

    return {
        'name': name,
        'group': group,
        'marks': marks,
    }
