import os

class Config:
    """docs"""

    SECRET_KEY = os.getenv('c0c6d740f7081aedf230858fb5bcbbfbbd24557a70a88419e97b110f2d22ac6b', 'c0c6d740f7081aedf230858fb5bcbbfbbd24557a70a88419e97b110f2d22ac6c')
    DEBUG = True

config = Config()

#will create env for securing this key generated