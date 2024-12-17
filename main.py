from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from flask import Flask
from flask_restx import Api

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)  # создаем движок для SQLAlchemyORM, для подключение к БД POSTGRES
metadata = MetaData()  # экземпляр для работы с метаданными БД
Session = sessionmaker(bind=engine)  # создаем сессию(подключение) к БД
Base = declarative_base()

app = Flask(__name__)
FlaskRestApi = Api(app, version="1.0", title="Twitter Service API", description="API for MicroBlogging service")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, host="0.0.0.0", port=8000)
