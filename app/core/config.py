import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Base(object):
    """
    Base config for flask app
    """

    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}".format(user='postgres',
                                                                                               password='postgres',
                                                                                               host='db',
                                                                                               port='5432',
                                                                                               database='postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = True

class DevelopmentConfig(Base):
    """
    Config for development env
    """
    pass



class ProductionConfig(Base):
    """
    Config for production env
    """
    DEBUG = False
