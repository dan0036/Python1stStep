phone_book = {}
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
        for i, contact in enumerate(contacts, 1):
            phone_book[i] = contact.strip().split(';')
            print(phone_book[i])

def exit():
    file = open(path, 'r')
    file.close()

def save_file():
    pass

def all_contacts():
    with open(path, 'r', encoding='UTF-8') as file:
        i = len(file.readlines())
        file.seek(0)
        while i:
            print(file.readline())
            i -= 1

def create_contact4():
    name = input('Введите имя: ')
    phone = input('Введите номер тел.: ')
    status = input('Введите ствтус: ')
    with open(path, 'a', encoding='UTF-8') as file:
        file.write('\n')
        file.write(str.join(';',[name, phone, status]))

def find_contact5():
    search = input('Введите данные для поиска: ')
    with open(path, 'r', encoding="UTF-8") as file:
        list_temp = file.readlines()
        for i in list_temp:
            if search in i:
                print(i)


def change_contact6():
    search = input('Выберите для поиска и отображения данные контакта, подлежащего изменению: ')
    with open(path, 'r') as file:
        str_temp = file.read()
        file.seek(0)
        list_temp = list(file.readlines())
        for i in list_temp:
            if search in i:
                search = i
                print(search)
                change = input('Скопируйте и вставьте строку контакта, внесите изменения и нажмите Enter: ')
                str_temp = str_temp.replace(search, change+'\n')
                print(str_temp)
                with open(path, 'w') as file2:
                    file2.write(str_temp)
                    break

def delete_contact7():
    search = input('Выберите для поиска и отображения данные контакта, подлежащего удалению: ')
    with open(path, 'r') as file:
        str_temp = file.read()
        file.seek(0)
        list_temp = list(file.readlines())
        for i in list_temp:
            if search in i:
                search = i
                print(search)
                deleter = input('Если этот контакт подлежит удалению, введите "да": ')
                if deleter == 'да':
                    str_temp = str_temp.replace(search, '')
                    print(str_temp)
                    with open(path, 'w') as file2:
                        file2.write(str_temp)
                        break
                else:
                    print('Начните процедуру заново.')

menu = '''Главное меню
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход'''

while True:
    print(menu)
    choice = input('Выберите пункт меню: ')
    match choice:
        case '1':
            open_file()
        case '2':
            save_file()
        case '3':
            all_contacts()
        case '4':
            create_contact4()
        case '5':
            find_contact5()
        case '6':
            change_contact6()
        case '7':
            delete_contact7()
        case '8':
            print('До свидания, всего хорошего!')
            exit()
            break
        case _:
            print('Ошибка ввода! Выберите пункт меню от 1 до 8')