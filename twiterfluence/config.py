import os

class Config:

    TWITTER_API_KEY = ''
    SECRET_KEY =   '***********your key'
    TWITTER_API_BASE_URL = 'https://api.twitter.com/1.1/users/lookup.json?screen_name=twitterapi,twitter/{}?api_key={}'.format(SECRET_KEY, TWITTER_API_KEY,)



    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://********your DB path'


class Config:

    """Main configurations class"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PITCH'
    SENDER_EMAIL = 'youremail@host.com'


class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    """Configuration class for development stage of the app"""

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
