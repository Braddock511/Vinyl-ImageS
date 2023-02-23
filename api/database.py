from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/postgres"

def get_credentials():
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

    return credentials

def post_data_image(data: list, image_url: str, with_price: bool = False, condition: str = ""):
    data = " ".join(data)

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

    data_to_insert = {"url":image_url, "data": data, "with_price": with_price, "condition": condition}
    data_image_instance = Data_Image(**data_to_insert)
    session.add(data_image_instance)
    session.commit()

    session.close()

def get_data_image():
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

    data_image = session.query(Data_Image).order_by(Data_Image.id.desc()).first()

    return data_image.data, data_image.url, data_image.with_price, data_image.condition