import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "friendlyeats-fastapi")
    FIRESTORE_EMULATOR_HOST = os.getenv(
        "FIRESTORE_EMULATOR_HOST",
        "127.0.0.1:8080"
    )


settings = Settings()