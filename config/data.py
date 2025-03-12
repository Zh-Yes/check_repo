import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    COVER_LETTER = os.getenv("COVER_LETTER")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    SOC_MEDIA_LINKS = os.getenv("SOC_MEDIA_LINKS")
    COMPANY_NAME = os.getenv("COMPANY_NAME")