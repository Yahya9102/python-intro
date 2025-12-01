from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
# Tom lista som vi kan använda för att spara våra usernames i 


users = []


from db import Base, engine, SessionLocal


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True,nullable=False)

    def __repr__(self):
        return f"User(id={self.id})"
    

Base.metadata.create_all(bind=engine)



def get_session() -> Session:
    
    return SessionLocal()






def add_user(name):

    # Rensa upp användarnamnet genom att ta bort eventuella mellanslag
    cleaned_name = name.strip()

    if len(cleaned_name) == 0:
        return False

    new_user = User(name=cleaned_name)


    with get_session() as session:
        session.add(new_user)
        try:
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False
    


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

