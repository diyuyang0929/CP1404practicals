name = input("Enter name: ")
print("(H)ello (G)oodbye (Q)uit")
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print(f"hello {name}")
    elif choice == "G":
        print(f"goodbye {name}")
    else:
        print("invalid message")
    print("(H)ello (G)oodbye (Q)uit")
    choice = input(">>> ")
print("finished message")
