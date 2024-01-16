
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "postgresql://muhammad.umair4084:ubP5XzAoqfY7@ep-wandering-shape-a5tyxf94.us-east-2.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



