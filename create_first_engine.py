from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

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

Session = sessionmaker(bind = engine)
session = Session()

book = Book(12132, "Soufi, mon amour", "Elif Shafak", "Ella Rubinstein a en apparence tout pour être heureuse", 2016)
session.add(book)