from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    ch_url: str = "clickhouse://default:@clickhouse:8123/"
    rabbit_url: str = "amqp://guest:guest@rabbitmq:5672/"

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        env_file=BASE_DIR / "config" / ".env",
    )


settings = Settings()
