from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ✅ Define database connection
DATABASE_URL = "sqlite:///company.db"  # Change to your database (e.g., MySQL, PostgreSQL)
engine = create_engine(DATABASE_URL, echo=True)

# ✅ Create Base
Base = declarative_base()

# ✅ Create a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
