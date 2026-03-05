import os

class Config:
    """Base configuration."""
    BYTEBLOC_API_URL = os.getenv('BYTEBLOC_API_URL')
    BYTEBLOC_API_KEY = os.getenv('BYTEBLOC_API_KEY')
    AI_MODEL_TYPE = os.getenv('AI_MODEL_TYPE', 'default_model')
    DATABASE_URI = os.getenv('DATABASE_URI')
    HOST = os.getenv('API_HOST', 'localhost')
    PORT = os.getenv('API_PORT', 5000)


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'sqlite:///dev.db')


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    DATABASE_URI = os.getenv('PROD_DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
