from .database import Base


class Company(Base):
    __tablename__ = "company"
    __table_args__ = {
        'autoload': True
    }
