from fastapi import APIRouter,Depends
from typing import Annotated
from pydantic import BaseModel, Field
from starlette import status
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Derivation



# Create a new router for derivation-related endpoints
router = APIRouter(
    prefix="/derivation",
    tags=['Derivation']
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]



class DerivationRequest(BaseModel):
    type: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=100)
    state: str = Field(min_length=3, max_length=50)
    migrate_situation: bool 
    sex:str = Field(min_length=1,max_length=3)
    age:int = Field(gt=0,lt=130)
    comuna:str = Field(min_length=3, max_length=50)
    region:str = Field(min_length=3, max_length=50)
     



# Endpoint to read all derivations
@router.get('/',status_code=status.HTTP_200_OK)
def read_all(db: db_dependency):
    return db.query(Derivation).all()

@router.post('/create',status_code=status.HTTP_201_CREATED)
def create_derivation(derivation: DerivationRequest, db: db_dependency):
    new_derivation = Derivation(**derivation.model_dump())
    db.add(new_derivation)
    db.commit()

    

