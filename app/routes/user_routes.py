from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas.schemas import UserSchema, RequestUser, Response
import utils.tools as tools


router = APIRouter()

counter = [0]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/v1/create_user")
async def create(request:RequestUser, db:Session=Depends(get_db)):
    tools.create_user(db,request.parameter)
    counter[0] +=1
    return Response(code=201, status="OK", message="Succesfully created").dict(exclude_none=True)

@router.get("/v1/get_all")
async def get(db:Session=Depends(get_db)):
    _user = tools.get_user(db,0,100)
    counter[0] +=1
    return Response(code=200, status="OK", message="Succefully found", result=_user).dict(exclude_none=True)

@router.get("/v1/get_user")
async def get_by_filter(id:int=None, name:str=None, lastname:str=None, email:str=None, db:Session=Depends(get_db)):
    _user = tools.get_users_filtered(db,user_id=id,name=name,lastname=lastname,email=email)
    counter[0] +=1
    print("USUARIO", _user)
    if _user is not None:
        return Response(code=200, status="OK", message="Succefully found", result=_user).dict(exclude_none=True)
    else:
        return Response(code=200, status="OK", message="User not found").dict(exclude_none=True)

@router.delete("/v1/delete_user")
async def delete(id:int, db:Session=Depends(get_db)):
    delete_status = tools.remove_user(db,user_id=id)
    counter[0] +=1
    if delete_status:
        return Response(code=203, status="OK", message="Succesfully deleted").dict(exclude_none=True)
    else:
        return Response(code=200, status="OK", message="User not found").dict(exclude_none=True)
