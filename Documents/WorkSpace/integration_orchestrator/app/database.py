import oracledb
from config import settings


class OracleDB:
    def __init__(self):
        self.con = oracledb.connect(
            user=settings.USER,
            password=settings.PASSWORD,
            config_dir=settings.CONFIG_DIR,
            wallet_location=settings.WALLET_LOCATION,
            wallet_password=settings.WALLET_PASSWORD,
            dsn=settings.DSN,
            encoding=settings.ENCODING,
        )

    @property
    def cursor(self):
        return self.con.cursor()

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()
