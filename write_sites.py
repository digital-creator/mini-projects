import csv

flag = True
print(
    '''
Добро пожаловать в хранилище сайтов!
Вам необходимо ввести название сайта и ссылку на сайт.
Данные автоматически сохраняться в файл.
Чтобы выйти из программы введите в названии сайта 'exit'
''')
while flag == True:
    name = str(input('Название сайта\n'))
    if name == 'exit':
        break
    link = str(input('Ссылка на сайта\n'))

    rows = {'name': name,
            'link': link
            }
            
    fieldnames = ['name', 'link']

    try:
        with open('sites.csv', 'r+') as file:
            
            parser = csv.DictWriter(f = file,
                                    fieldnames = fieldnames,
                                    delimiter = ','
                                    )
            
            line = file.readline()
            if len(line) <= 1:
                parser.writeheader()
            parser.writerow(rows)
    except Exception as e:
        print(e)
        with open('sites.csv', 'w') as file:
            parser = csv.DictWriter(f = file,
                                    fieldnames = fieldnames,
                                    delimiter = ',')
            parser.writeheaders()

