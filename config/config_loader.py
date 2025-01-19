from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

class Config:
    @staticmethod
    def get_env_var(key, default=None):
        return os.getenv(key, default)

    @staticmethod
    def get_static_config():
        with open("config/static_config.json", "r") as f:
            return json.load(f)
