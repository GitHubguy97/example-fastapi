from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str  # This must match the corrected env var in .env
    database_name: str  # Add this since it's in the .env file
    secret_key: str  # Fix the typo from `secrete_key` to `secret_key`
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()
