from datetime import datetime as dt, timedelta  # импорт класса datetime
current_datetime = dt.now()
print("Текущая дата" , current_datetime)

def uni(list_, title_):                 # проверка уникальности заметки
    if list_ is not None:
        if title_ in list_:
            return False
    return True

def status_update():
    print(
        '\nВыберите новый статус Вашей заметки. Для продолжение нажмите ENTER. :'   # Функция обновления статуса заметки
        '\n1. В процессе \n2. Отложено \n3. Выполнено'
    )
    while True:
        ans = input()
        if ans == '1':
            notes['status'] = 'В процессе'
            break
        elif ans == '2':
            notes['status'] = 'Отложено'
            break
        elif ans == '3':
            notes['status'] = 'Выполнено'
            break
        else:
            print('Ошибка, попробуйте снова.')
    print(
        f'\nСтатус обновлен. Текущий статус: '
        f'{notes.get("status").upper()}'
    )

    input("\nДля продолжения нажмите ENTER.")
    return True

def print_note_data(notes):                      # Вывод данных
    print('\nВведенные данные:')
    for key, value in notes.items():
        if type(value) == dt:
            print(f'| {key.capitalize()}: {value:%d %b}')
            continue
        elif type(value) == list:
            print(f'| {key.capitalize()}: {", ".join(value)}')
            continue
        print(f'| {key.capitalize()}: {value}')

    deadline_delta_days = f_deadline_check()
    if deadline_delta_days > 0:
        print(
            f'\nДата выполнения истекла '
            f'{deadline_delta_days} дней назад'
        )
    elif f_deadline_check() < 0:
        print(f'\nДней до истечения заметки: '
              f'{str(deadline_delta_days)[1:]}')
    elif f_deadline_check() == 0:
        print('\nДата истечения заметки сегодня!')


def f_deadline_check():
    day_delta = dt.today() - notes.get('issue_date')
    return day_delta.days

notes = {}
notes['username'] = input('Введите имя пользователя: ')
notes['content'] = input("Введите содержание заметки: ")
notes['status'] = 'В процессе'
notes['created_date'] = dt.today()

while True:
    try:
        parsed_issue_date: dt = \
            dt.strptime(input
                (
                'Введите дату в формате DD.MM.YYYY : '
            ), '%d.%m.%Y'
            )
    except ValueError:
        print('Неверная дата, попробуйте снова.')
    else:
        break
notes['issue_date'] = parsed_issue_date

while True:
    title_str = input(
        '\nВведите заголовок или оставьте пустым для завершения. '
        'Для продолжения нажмите ENTER. : '
    )
    if title_str != '':
        if uni(notes.get('titles'), title_str):
            # if key doesnt exist in dict it will be added as list
            notes.setdefault('titles', []).append(title_str)
        else:
            print('Этот заголовок уже существует!')
    else:
        print('\nВаши заголовки:')
        if notes.get('titles') is not None:
            for title in notes.get('titles'):
                print(title)
            break
        else:
            print("Необходим минимум один заголовок")
print_note_data(notes)

while True:
    choice = input(
        '\nХотите изменить статус Вашей заметки? (yes/no, +/-, да/нет)'
    ).lower()
    if choice in ['yes', 'y', '+', 'да'] and status_update():
        print_note_data(notes)
    elif choice in ['no', 'n', '-', 'нет']:
        print('Хорошая работа. До новых встреч!')
        break
    else:
        print('Ошибка, попробуйте снова :(')
