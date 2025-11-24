from colorama import Fore, Style
from rich import print

def main():
    dishes = []
    while True:
        print(Fore.RED +"\n------Meny------" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Lägg till maträtt" + Style.RESET_ALL)
        print("[red]2. Lista alla maträtter[/red]")
        print("3. Ändra maträtt")
        print("4. Lunchmeny")
        print("0. Avsluta")


        selection = input("Välj ett alternativ (0-4):").strip()

        if selection == "1":
            name = input("Maträttens namn: ").strip()
            print(f"Längd: {len(name)}")

            dishes.append(name)
            print(f"Maträtten '{name}' har lagts till i menyn.")

        elif selection == "2":
            print ("\nAlla maträtter i menyn:")    
            for dish in dishes:
                print("- " + dish)
            print("-------------------")    

        elif selection == "3":
            print("\nÄndra maträtt")

        elif selection == "4":
            print("\nLunchmeny")

        elif selection == "0":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val. Försök igen.")    


if __name__ == "__main__":
    main()


"""


from .users import add_user, list_users, user_exists, delete_user


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