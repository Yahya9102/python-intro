# Tom lista som vi kan använda för att spara våra usernames i 
users = []


def add_user(name):

    # Rensa upp användarnamnet genom att ta bort eventuella mellanslag
    cleaned_name = name.strip()

    if len(cleaned_name) == 0:
        return False

    # Kontrollera om användarnamnet redan finns i listan 
    if cleaned_name in users:
        return False

    users.append(cleaned_name)
    return True


# CHECK
def list_users():
    return users


# CHECK 
def user_exists(name):

    cleaned_name = name.strip()
    if cleaned_name in users:
        return True, f"Användare '{cleaned_name}' finns i listan."
    else:
        return False, f"Användare ''{cleaned_name} finns inte i listan."
    



def delete_user(name):

    cleaned_name = name.strip()


    if cleaned_name in users:
        users.remove(cleaned_name)
        return True, f"Användare '{cleaned_name}' har tagits bort."
    else:
        return False, f"Användare '{cleaned_name}' finns inte i listan."

