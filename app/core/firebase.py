import os
from google.auth.credentials import AnonymousCredentials
from google.cloud import firestore
from app.core.config import settings


# Configurar el emulador de Firestore
os.environ["FIRESTORE_EMULATOR_HOST"] = settings.FIRESTORE_EMULATOR_HOST

# Conectar con Firestore sin credenciales de Google Cloud
db = firestore.Client(
    project=settings.PROJECT_ID,
    credentials=AnonymousCredentials()
)