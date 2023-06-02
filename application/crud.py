from sqlalchemy.orm import Session
from . import models, schemas


def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()


def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(
        name=company.name,
        address=company.address,
        phone_number=company.phone_number,
        website=company.website,
        industry=company.industry,
        size=company.size,
        founded=company.founded)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(company_id: int, db: Session, company: schemas.CompanyUpdate):
    db_company = db.query(models.Company).filter(
        models.Company.id == company_id).first()
    db_company.name = company.name
    db_company.address = company.address
    db_company.founded = company.founded
    db_company.industry = company.industry
    db_company.phone_number = company.phone_number
    db_company.size = company.size
    db_company.website = company.website
    db.commit()
    db.refresh(db_company)
    return db_company


def get_company_by_name(db: Session, name: str):
    return db.query(models.Company).filter(models.Company.name == name).first()


def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).filter(
        models.Company.id == company_id).first()
    db.delete(db_company)
    db.commit()
    return db_company


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, db: Session, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.email = user.email
    db_user.is_active = user.is_active
    db.commit()
    db.refresh(db_user)
    return db_user
