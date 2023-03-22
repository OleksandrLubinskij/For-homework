print('Hello User!')

try:
    with open('save-to-file.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')

number = None
while True:
    a = int(input('\n1 - Set\n2 - Null\n3 - Exit\n\nChoose action: '))
    if a == 1:
        num = int(input('Enter number: '))
        number = num
        with open('save-to-file.txt', 'w', encoding='utf-8') as file:
            file.write(f'The number you guessed - {str(number)}')
        print(f'You set - {number}')

    elif a == 2:
        number = 0
        print(number)

    elif a == 3:
        print('Bye!')
        break
