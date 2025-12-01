from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
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
    
    with get_session() as session:
        users = session.query(User).all()
        return [u.name for u in users]


# CHECK 
def user_exists(name):

    cleaned_name = name.strip()
    
    with get_session() as session:
        user = session.query(User).filter(User.name == cleaned_name).first()

        if user:
            return True, f"Användare '{cleaned_name}' finns i listan."
        else:
            return False, f"Användare '{cleaned_name}' finns inte i listan"




def delete_user(name):

    cleaned_name = name.strip()


    with get_session() as session:
        user = session.query(User).filter(User.name == cleaned_name).first()

    
    if not user:
        return False, f"Användare '{cleaned_name}' finns inte i listan."
    
    session.delete(user)
    session.commit()
    return True, f"Användare '{cleaned_name}' har tagits bort"



def update_user(old_name: str, new_name: str):

    cleaned_old = old_name.strip()
    cleaned_new = new_name.strip()

    if len(cleaned_new) == 0:
        return False, "Kan inte vara tom"
    
    with get_session() as session:
        user = session.query(User).filter(User.name == cleaned_old).first()

        if not user:
            return False, f"Användare '{cleaned_old}' finns inte med i listan"
        

        exisiting = session.query(User).filter(User.name == cleaned_new).first()
        if exisiting:
            return False, f"Användare '{cleaned_new}' finns redan i listan"
        
        user.name = cleaned_new
        session.commit()
        return True, f"Användare '{cleaned_old}' har uppdaterats till '{cleaned_new}'"
    
