import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


class TestConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-you-will-never-guess'
