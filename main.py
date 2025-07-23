print('Hello')

print('How can i help you')

print(input('Hello: '))


def main():
    while True:
        ask= input("How can i help you?: ")
        if ask.lower() == 'add':
            ask_name = input('Enter the name: ')
            ask_phone = input("Enter the number: ")

            name_number_dict = {ask_name: ask_phone}

        elif ask.lower() == 'exit':
            print('Good bye!')
            break
        elif ask.lower() == 'close':
            print('Good bye!')
            break
        elif ask.lower() == 'change':
            print(name_number_dict)
            ask_name2 = input('Enter the name you want to change: ')

            name_number_dict.pop(ask_name2)
            new_name = input('Enter the new namber: ')
            new_number = input("Enter the new number: ")
            name_number_dict = {new_name: new_number}
        elif ask.lower() == 'phone':
            ask3 = input("Enter the people name that number you want to know: ")
            if ask3 in name_number_dict:
                print(name_number_dict(ask3))
            else:
                print('name that you wrote has never been at this dict')            
        elif ask.lower() == 'all':
            print(f'the all names and numbers that in dict: {name_number_dict}')
        else:
            print("Invalid command, please write add, change, all, exit")

        

if __name__ == "__main__":
    main()
