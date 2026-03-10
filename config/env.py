import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("TEST_USERNAME")
PASSWORD = os.getenv("TEST_PASSWORD")
