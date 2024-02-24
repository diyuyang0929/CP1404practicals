MENU = "(G)et a valid score,(P)rint result,(S)how stars,(Q)uit"
print(MENU)


def main():
    score = get_valid_score()
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("invalid input error message")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter your score: "))
    return score


def print_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("passable")
    else:
        print("Bad")


def show_stars(score):
    print("*" * int(score))


main()
