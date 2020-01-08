import os
from secrets import token_hex
from redis import Redis


class Config(object):
    """Configuration of app properties"""
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'production'
    REDIS_HOST = os.environ.get('REDIS_HOST') or 'localhost'

    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(REDIS_HOST)
    PERMANENT_SESSION_LIFETIME = 60 * 15
    SESSION_COOKIE_SECURE = FLASK_ENV == 'production'

    SECRET_KEY = os.environ.get('SECRET_KEY') or token_hex(1024)
