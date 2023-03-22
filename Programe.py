print('Hello User!')

number = None
while True:
    a = int(input('\n1 - Set\n2 - Null\n3 - Exit\n\nChoose action: '))
    if a == 1:
        num = int(input('Enter number: '))
        number = num
        print(number)
    elif a == 2:
        number = 0
        print(number)
    elif a == 3:
        print('Bye!')
        break