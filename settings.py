from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    """Environmental variables for registration to linkedin"""

    linkedin_gmail: SecretStr
    linkedin_password: SecretStr

    class Config:
        """The source of environmental variables""" 
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Settings() # type: ignore