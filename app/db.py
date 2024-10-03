# db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.module import ChatMessageDB, Base  # Import model from models.py

# Define the database URL (can be SQLite or any other supported DB)
DATABASE_URL = "sqlite:///./test.db"

# Set up the database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the messages table in the database
Base.metadata.create_all(bind=engine)

# Function to save chat message and response to the database
def save_message_to_db(message, response):
    db = SessionLocal()
    db_message = ChatMessageDB(message=message, response=response)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    db.close()
