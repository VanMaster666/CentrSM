from sqlalchemy.orm import Session
from sqlalchemy import text
from models import Users, Roles

def get_users(db: Session):
    return db.execute(text("SELECT * FROM USERS")).fetchall()

def get_roles(db: Session):
    return db.execute(text("SELECT * FROM ROLES_LAYOUT")).fetchall()