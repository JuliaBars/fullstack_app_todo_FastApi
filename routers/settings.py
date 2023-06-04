import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", 'fsdamh53263')
ALGORITHM = os.getenv("ALGORITHM", 'HS256')
