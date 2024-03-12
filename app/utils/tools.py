from sqlalchemy.orm import Session
from models.model import User
from schemas.schemas import UserSchema
from sqlalchemy import or_
import asyncio


# Get all users data
def get_user(db:Session, skip:int=0, limit:int=100):
    return db.query(User).offset(skip).limit(limit).all()

# Get user by id, name, lastname, or email
def get_users_filtered(db: Session, user_id:int = None, name:str = None, lastname:str = None, email:str = None):
    query = db.query(User)
    conditions = []
    if user_id is not None:
        conditions.append(User.id == user_id)
    if name is not None:
        conditions.append(User.name == name)
    if lastname is not None:
        conditions.append(User.lastname == lastname)
    if email is not None:
        conditions.append(User.email == email)

    if conditions:
        query = query.filter(or_(*conditions))
        print(query)

    return query.first()

# Create user
def create_user(db:Session, user:UserSchema):
    _user = User(name=user.name,lastname=user.lastname, email=user.email)
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

# Remove user
def remove_user(db:Session, user_id:int):
    _user = get_users_filtered(db=db, user_id=user_id)
    if _user is not None:
        db.delete(_user)
        db.commit()
        return True
    else:
        return False
    

# Calling counter timer
counter_timer = [0]

async def increment_counter():
    while True:
        await asyncio.sleep(60*5)   # 5 minutes
        global counter_timer
        counter_timer[0] += 1
        print("here",counter_timer )

loop = asyncio.get_event_loop()
loop.create_task(increment_counter())

