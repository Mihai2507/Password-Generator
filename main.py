from Generator import generate_password

if __name__ == '__main__':
    while True:
        length = int(input('Enter length of password: '))
        generate_password(length)
        choice = input('Would you like to generate another password? (y/n):\n')
        if choice == 'y':
            length2 = int(input('Enter length of password: '))
            generate_password(length2)
        elif choice == 'n':
            break
