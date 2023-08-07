from models import engine, Composer, Song, Contributor
from faker import Faker
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    session.query(Composer).delete()
    session.query(Contributor).delete()
    session.query(Song).delete()
    # session.query(Sheet).delete()

    composers = []
    for _ in range(10):
        composer = Composer(name=f"{fake.first_name()} {fake.last_name()}")
        session.add(composer)
        session.commit()
        composers.append(composer)

    songs = [
        Song(
            name="Twinkle Twinkle Little Star",
            sheet="C C G G A A 2 G G G F F D D 2S",
            tempo=100,
        ),
        Song(
            name="Fur Elise",
            sheet="+F +R +F +R +F K +D +S 2J S F J 2K F Y K 2S F +F +R +F +R +F K +D +S 2J S F J 2K D +S K 4J",
            tempo=136,
        ),
    ]
    session.add_all(songs)
    session.commit()
    session.close()
