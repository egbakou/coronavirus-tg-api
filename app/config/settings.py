"""app.config.settings.py"""
import os

# Load environment variables from .env file.
from dotenv import load_dotenv

load_dotenv()

# The port to serve the app application on.
PORT = int(os.getenv("PORT", "5000"))
