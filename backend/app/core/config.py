import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")

        if not self.DATABASE_URL:
            raise RuntimeError("DATABASE_URL environment variable is required")


settings = Settings()
