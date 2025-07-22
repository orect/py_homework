import time

print('Hello')
time.sleep(2)
print('How can i help you')

def add_contact():
    while True:
        time.sleep(2)
        user_ask1 = input('введіть add якщо ви хочете додати ім\'я і номер телефону: ')
        if user_ask1.lower() == 'add':

            global add_name
            global add_number


            time.sleep(2)
            add_name = input('введіть ім\'я: ')
            add_number = input('Введіть номер телефону який ви хочете додати: ')
            time.sleep(1)
            print('Зберігаю інформацію...')
            time.sleep(3)


            global name_number_dict
            name_number_dict = {add_name: add_number} 
            print(name_number_dict)

            user_ask2 = input('Чи хочете ви ще ввести? Так/ні:  ')
            if user_ask2.lower() == 'так':
                pass
            
            else:
                print('Ця інформація збережена!')
                break

        else:
            print('ви вводете не те що вас просять :(')
    

def change_contact():
    user_ask1 = input('Чи бажаєте ви змінити конткакт так/ні: ')
    if user_ask1.lower() == 'так':
        time.sleep(1)
        add_name = input('Введіть на яке ім\'я ви бажаєте змінити: ')
        add_number = input('Введіть номер телефону на який ви бажаєте змінити: ')
        time.sleep(1)
        print('виконую зміну')
        name_number_dict.pop(add_name)

        name_number_dict[add_name] = add_number
        print(name_number_dict)

        time.sleep(3)
        print('змінну успішно збережено!')

add_contact()
change_contact()

def show_phone():
    while True:
        ask = input('щоб дізнатись телефон напишіть ім\'я користувача номером: ')
        
        if ask == add_name:
            print(add_number)
        else:
            break

show_phone()

def all():
    ask = input("якщо ви хочете дізнатись всі ім'я і номера в записній книжці напишіть так/ні: ")
    while True:
        if ask == 'так':
            print(name_number_dict)
        
        else:
            break
def close_exit():
    ask = input("Чи бажаєте ви завершити прогрмму? так/ні: ")
    while True:
        if ask == 'так':
            ask2 = input('введіть: close or exit: ')
            if ask2 == 'close':
                break
            if ask2 == 'exit':
                break
        else:
            print("программа почнеться заново")

close_exit()