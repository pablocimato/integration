from os import getenv


class BaseConfig:
    """Database environment variables."""

    USER: str = getenv("DB_USER")
    PASSWORD: str = getenv("DB_PASSWORD")
    CONFIG_DIR: str = getenv("DB_CONFIG_DIR")
    WALLET_LOCATION: str = getenv("DB_WALLET_LOCATION")
    WALLET_PASSWORD: str = getenv("DB_WALLET_PASSWORD")
    DSN: str = getenv("DB_DSN")
    ENCODING: str = getenv("DB_ENCODING")

    """Encrypting and decrypting environment variables"""
    AES_PASSWORD: str = getenv("AES_PASSWORD")


settings = BaseConfig()
