import os

class Settings:
    BASE_URL = os.environ['API_BASE_URL'] if os.environ['API_BASE_URL'] else 'https://api.international-design.pro/'
    SANDBOX_BASE_URL = os.environ['API_SANDBOX_BASE_URL'] if os.environ['API_SANDBOX_BASE_URL'] else 'https://api.international-design.pro/'

settings = Settings()