from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import update
from sqlalchemy import delete


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    author:  Mapped[str] = mapped_column(String(30))
    description:  Mapped[str] = mapped_column(String(200))
    year_published: Mapped[int] = mapped_column(Integer())
    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, title={self.title!r}, author={self.author!r}, description={self.description!r}, year_published={self.year_published!r})"

engine = create_engine("sqlite:///./db/Alexandria.db", echo=True)

Base.metadata.create_all(bind = engine)

with Session(engine) as session:
    # b1 = Book(
    #     id = 92842,
    #     title="Soufi, mon amour",
    #     author="Elif Shafak",
    #     description="Ella Rubinstein a en apparence tout pour être heureuse",
    #     year_published = 2009,
    # )
    # b2 = Book(
    #     id = 12134,
    #     title = "La bâtarde d'instanbul",
    #     author = "Elif Shafak",
    #     description = "description 2",
    #     year_published = 2006,
    # )
    # b3 = Book(
    #     id = 39281,
    #     title = "The Island of missing tres",
    #     author = "Elif Shafak",
    #     description = "description 3",
    #     year_published = 2009,
    # )
    # b4 = Book(
    #     id = 12192,
    #     title = "Goobye to shy",
    #     author = "Leil Lowndes",
    #     description = "Not being shy anymore",
    #     year_published = 2009,
    # )
    # b5 = Book(
    #     id = 34532,
    #     title = "La quête du Joyau",
    #     author = "hams ed Dîn Tabrîzî",
    #     description = "description 5",
    #     year_published = 2001,
    # )
    # session.add_all([b1, b2, b3, b4, b5])
    # session.commit()
    pass #Uncomment this if the database doesn't exist yet

results = session.query(Book).all() #Retrieving all books
print(results)

elif_shafak = session.query(Book).filter(Book.author == "Elif Shafak") #Retrieving all books written by a specific author
for book in elif_shafak:
    print(book)

book = session.query(Book).filter(Book.id == 39281).first()
book.year_published = 2000
session.commit()
