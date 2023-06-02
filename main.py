from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from application import crud, models, schemas
from application.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/createcompany/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = crud.get_company_by_name(db, company.name)
    if db_company:
        raise HTTPException(status_code=400, detail="Company already exists")
    return crud.create_company(db=db, company=company)


@app.put("/updatecompany/", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyUpdate, db: Session = Depends(get_db)):
    return crud.update_company(company_id, db=db, company=company)


@app.get("/companies/", response_model=list[schemas.Company])
def read_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_companies(db, skip=skip, limit=limit)
    return companies


@app.delete("/deletecompany/", response_model=schemas.Company)
def del_company(company_id: int, db: Session = Depends(get_db)):
    company = crud.delete_company(db, company_id)
    return company


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/updateuser/", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(user_id, db, user)


@app.delete("/deleteuser/", response_model=schemas.User)
def del_company(user_id: int, db: Session = Depends(get_db)):
    company = crud.delete_user(db, user_id)
    return company


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
