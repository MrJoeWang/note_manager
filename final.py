username = input("Введите имя пользователя: ")
title1 = input("Введите заголовок 1 заметки:  ")
title2 = input("Введите заголовок 2 заметки:  ")
title3 = input("Введите заголовок 3 заметки:  ")
titles = [title1, title2, title3]
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки в формате "день-месяц-год" : ')
note = [username, titles, content, status, created_date, issue_date]
note_book = {"Имя пользователя" : username, "Заголовок заметки" : titles, "Описание заметки" : content, "Статус заметки" : status,
             "Дата создания заметки" : created_date[:5],"Дата исчезновения заметки" : issue_date[:5]}

for key, value in note_book.items():
    if type(value) == list:
        print(f'{key}: {", ".join(value)}')
    else: print("{0}: {1}".format(key,value))


