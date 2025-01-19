from .sql_database import SQLDatabase
from .nosql_database import NoSQLDatabase
from .google_sheets_database import GoogleSheetsDatabase
from config_loader import Config

def get_database():
    db_type = Config.get_env_var("DATABASE_TYPE", "SQL").upper()
    if db_type == "SQL":
        return SQLDatabase()
    elif db_type == "NOSQL":
        return NoSQLDatabase()
    elif db_type == "GOOGLE_SHEETS":
        return GoogleSheetsDatabase()
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
