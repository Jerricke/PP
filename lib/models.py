from sqlalchemy import (
    ForeignKey,
    create_engine,
    Column,
    String,
    Integer,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///piano.db")

Base = declarative_base()


class Composer(Base):
    __tablename__ = "composers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<id: {self.id}> \n \
            + <name: {self.name}"


class Contributor(Base):
    __tablename__ = "contributors"

    id = Column(Integer(), primary_key=True)
    composer_id = Column(Integer(), ForeignKey("composers.id"))
    composer = relationship("Composer", backref="contributors")
    song_id = Column(Integer(), ForeignKey("songs.id"))
    song = relationship("Song", backref="contributors")

    def __repr__(self):
        return f"<id: {self.id}> \n \
            + <name: {self.name}> \n \
            + <composer_id: {self.composer_id}> \n \
            + <song_id: {self.song_id}>"


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    length = Column(Float())
    sheet = Column(String())
    tempo = Column(Integer())

    def __repr__(self):
        return f"<id: {self.id}> \n \
            + <name: {self.name}> \n \
            + <length: {self.length}> \n \
            + <sheet: {self.sheet}>"


# class Sheet(Base):
#     __tablename__ = "sheets"

#     id = Column(Integer(), primary_key=True)
#     song_id = Column(Integer(), ForeignKey("songs.id"))
#     song = relationship("Song", backref="sheets")
#     sequence = Column(String())

#     def __repr__(self):
#         return f"<id: {self.id}> \n \
#             + <song_id: {self.song_id}> \n \
#             + <sequence: {self.sequence}>"
