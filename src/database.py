from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connexion a la base de donnée et déclaration de la base avec sql alchemy

# url de connexion de la base
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost/fromagerie_com"
                        # connector : mysql / mysql+pymysql
                        # utilisateur : root
                        # password : root
                        # base de données : fromagerie_com
                        

# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
