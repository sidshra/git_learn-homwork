from typing import Optional

from fastapi import FastAPI,HTTPException

from sqlmodel import Field, SQLModel, Session, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# hero = Hero(name="Lord-of-Thunder", secret_name="Chris Hemsworth    ")
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Part 1 - POST method for insert into table hero for the first time
@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()


# Part 2 - GET values from table based on given hero name
@app.get("/heroes/{name}")
def get_hero(name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == name)
        hero = session.exec(statement).first()
        if hero != None:
            return hero
        else:
            raise HTTPException(status_code=404, detail="Item not found")


# Part 3 - GET all heroes from table here
@app.get("/heroes/")
def get_hero():
    with Session(engine) as session:
        statement = select(Hero)
        heroes = session.exec(statement).all()
        return heroes
