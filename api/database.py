from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# define the database URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/postgres"

def get_credentials():
    # create the engine and session to interact with the database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    class Credentials(Base):
        __tablename__ = "credentials"

        id = Column(Integer, primary_key=True, index=True)

        api_imagekit_id = Column(String)
        api_imagekit_secret = Column(String)
        api_imagekit_endpoint = Column(String)

        api_azure_subscription_key = Column(String)
        api_azure_endpoint = Column(String)

        api_discogs_id = Column(String)
        api_discogs_secret = Column(String)
        api_discogs_token = Column(String)

    # create the table if it does not exist
    Base.metadata.create_all(engine)

    rows = session.query(Credentials).all()
    credentials = []

    for row in rows:
        credentials.append(row.api_imagekit_id)
        credentials.append(row.api_imagekit_secret)
        credentials.append(row.api_imagekit_endpoint)

        credentials.append(row.api_azure_subscription_key)
        credentials.append(row.api_azure_endpoint)

        credentials.append(row.api_discogs_id)
        credentials.append(row.api_discogs_secret)
        credentials.append(row.api_discogs_token)

    session.close()
    
    return credentials

def post_data_image(data: list, image_url: str, with_price: bool = False, condition: str = ""):
    # create the engine and session to interact with the database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()

    class Data_Image(Base):
        __tablename__ = "data_image"
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        url = Column(String)
        data = Column(String)
        with_price = Column(Boolean)
        condition = Column(String)

    # create the table if it does not exist
    Base.metadata.create_all(engine)

    # create a dictionary of the data to be inserted into the data_image
    data_to_insert = {"url":image_url, "data": data, "with_price": with_price, "condition": condition}
    data_image_instance = Data_Image(**data_to_insert)

    # add the instance to the session, commit and close the session to save the data to the database
    session.add(data_image_instance)
    session.commit()
    session.close()

def get_data_image():
    # create the engine and session to interact with the database
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base = declarative_base()

    Session = sessionmaker(bind=engine)
    session = Session()
    
    class Data_Image(Base):
        __tablename__ = "data_image"

        id = Column(Integer, primary_key=True, index=True)
        url = Column(String)
        data = Column(String)
        with_price = Column(Boolean)
        condition = Column(String)

    # retrieve the most recent row from the data_image table
    data_image = session.query(Data_Image).order_by(Data_Image.id.desc()).first()
    session.close()

    return data_image.data, data_image.url, data_image.with_price, data_image.condition