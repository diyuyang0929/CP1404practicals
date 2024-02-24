MINIMUM_LENGTH = 6


def question_1():
    password = input(f"Enter your password at the least of {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter your password at the least of {MINIMUM_LENGTH} characters: ")
    print('*' * len(password))


question_1()


def main():
    get_password()


def get_password():
    password = input(f"Enter your password at the least of {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter your password at the least of {MINIMUM_LENGTH} characters: ")
    asterisks(password)


def asterisks(password):
    print('*' * len(password))


main()
