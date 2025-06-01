from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import *
from app.global_config import db_config
from app.utils.logging import info, error
from time import sleep

class Database():
    _instance = None
    _engine = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._engine = cls._instance.get_engine_from_config()
        return cls._instance

    def get_engine(self, user, pwd, host, port, db):
        url = f'postgresql://{user}:{pwd}@{host}:{port}/{db}'

        try:
            if not database_exists(url):
                create_database(url)
                info(f'Database {db} created', __file__)
            engine = create_engine(url, pool_size=db_config["poolsize"], echo=db_config["debug"])
            info(f'Connected to database {db}', __file__)
        except Exception as e:
            error(f'Error connecting to database {db}: {e}. Trying to reconnect...', __file__)
            sleep(3)
            return self.get_engine(user, pwd, host, port, db)
        return engine
    
    def get_engine_from_config(self):
        keys = ['pguser', 'pgpassword', 'pghost', 'pgport', 'pgdb']
        if not all(key in db_config for key in keys):
            raise KeyError(f'Bad database config file. Ensure all keys are present: {keys}')
        
        return self.get_engine(
            user = db_config['pguser'],
            pwd = db_config['pgpassword'],
            host = db_config['pghost'],
            port = db_config['pgport'],
            db = db_config['pgdb']
        )
    
    @staticmethod
    def get_session():
        if Database._engine == None:
            error(f"Database is not initialized. Perhap you forget to create a new instance of Database?", __name__)
            raise RuntimeError()
        session = sessionmaker(bind=Database._engine)()
        return session
    

    