username = input("Введите имя пользователя: ")
titles = []
title = input("Введите заголовок: ")
titles.append(title)
while True:
    title = input("Введите заголовок или оставьте пустым для завершения: ")

    if not title:
        break
    titles.append(title)
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки в формате "день-месяц-год" : ')
note = [username, titles, content, status, created_date, issue_date]
note_book = {"Имя пользователя" : username, "Заголовок заметки" : titles, "Описание заметки" : content, "Статус заметки" : status,
             "Дата создания заметки" : created_date[:5],"Дата истечения заметки" : issue_date[:5]}

for key, value in note_book.items():
    if type(value) == list:
        print(f'{key}: {", ".join(value)}')
    else: print("{0}: {1}".format(key,value))
