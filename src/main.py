
from .server import run_server


def main():
    run_server()


if __name__ == "__main__":
    main()


""""
def show_menu():
    print("1. Lägg till användare")
    print("2. Lista alla användare")
    print("3. Kontrollera om användaren finns")
    print("4. Ta bort användare")
    print("5. Avsluta")



def handle_search_user():
    name = input("Ange ett användarnamn: ")
    exists, message = user_exists(name)
    print(exists,message)




def handle_add_user():
    name = input("Ange ett användarnamn: ")
    sucess = add_user(name)

    if sucess:
        print(f"Användaren'{name.strip()}' lades till" )
    else:
        print("Kunde inte lägga till användare")
        print(" Namnet kanske är tom eller redan finns")    


def handle_list_users():
    all_users = list_users()

    if len(all_users) == 0:
        print("Det finns inga användare i listan..")
    else:
        for index, name in enumerate(all_users, start=1):
            print(f"{index}, {name}")    


def handle_delete_user():
    name = input("Ange ett användarnamna att ta bort")
    sucess, message = delete_user(name)
    print(sucess, message)


def main():
    while True:
        show_menu()

        choice = input("Välj ett alternativ: ").strip()
        
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            handle_list_users()
        elif choice == "3":
            handle_search_user()
        elif choice == "4": 
            handle_delete_user()
        elif choice == "5":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")



if __name__ == "__main__":
    main()



"""    