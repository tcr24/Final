from pydantic_settings import BaseSettings
from pydantic import Field, AnyUrl

class Settings(BaseSettings):
    max_login_attempts: int = Field(default=3, description="Background color of QR codes")
    server_base_url: AnyUrl = Field(default='http://localhost', description="Base URL of the server")
    server_download_folder: str = Field(default='downloads', description="Folder for storing downloaded files")
    secret_key: str = Field(default="secret-key", description="Secret key for encryption")
    algorithm: str = Field(default="HS256", description="Algorithm used for encryption")
    access_token_expire_minutes: int = Field(default=30, description="Expiration time for access tokens in minutes")
    admin_user: str = Field(default='admin', description="Default admin username")
    admin_password: str = Field(default='secret', description="Default admin password")
    debug: bool = Field(default=False, description="Debug mode outputs errors and sqlalchemy queries")
    jwt_secret_key: str = "a_very_secret_key"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 15  # 15 minutes for access token
    refresh_token_expire_minutes: int = 1440  # 24 hours for refresh token
    database_url: str = Field(default='postgresql+asyncpg://user:password@postgres/myappdb', description="URL for connecting to the database")
    postgres_user: str = Field(default='user', description="PostgreSQL username")
    postgres_password: str = Field(default='password', description="PostgreSQL password")
    postgres_server: str = Field(default='localhost', description="PostgreSQL server address")
    postgres_port: str = Field(default='5432', description="PostgreSQL port")
    postgres_db: str = Field(default='myappdb', description="PostgreSQL database name")
    discord_bot_token: str = Field(default='NONE', description="Discord bot token")
    discord_channel_id: int = Field(default=1234567890, description="Default Discord channel ID for the bot to interact", example=1234567890)
    openai_api_key: str = Field(default='NONE', description="Open AI Api Key")
    send_real_mail: bool = Field(default=False, description="use mock")
    smtp_server: str = Field(default='sandbox.smtp.mailtrap.io', description="SMTP server for sending emails")
    smtp_port: int = Field(default=2525, description="SMTP port for sending emails")
    smtp_username: str = Field(default='tcr24', description="Username for SMTP server")
    smtp_password: str = Field(default='TRubiconnor101!?', description="Password for SMTP server")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
