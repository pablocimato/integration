import os
import subprocess
from config import settings


class AESCipher:
    """Class to mange AES Cipher."""

    _password = settings.PASSWORD

    @classmethod
    def decrypt_all_files(cls, dir_in, dir_out):
        file_names = os.listdir(dir_in)
        for file_name in file_names:
            cls.decrypt_file(file_name, dir_in, dir_out)
        return True

    @classmethod
    def encrypt_all_files(cls, dir_in, dir_out):
        file_names = os.listdir(dir_in)
        for file_name in file_names:
            cls.decrypt_file(file_name, dir_in, dir_out)
        return True

    @classmethod
    def decrypt_file(cls, file_name, dir_in, dir_out):
        in_path = dir_in + file_name
        out_path = dir_out + file_name.replace(".enc", "")
        try:
            subprocess.run(
                [
                    "openssl",
                    "aes-256-cbc",
                    "-d",
                    "-salt",
                    "-pbkdf2",
                    "-in",
                    in_path,
                    "-out",
                    out_path,
                    "-pass",
                    "pass:" + cls._password,
                ],
                check=True,
            )
        except Exception as ex:
            print(f"error decrypting file: {file_name} ex: {ex}")

        return True

    @classmethod
    def encrypt_file(cls, file_name, dir_in, dir_out):
        out_path = dir_in + file_name + ".enc"
        in_path = dir_out + file_name
        try:
            subprocess.run(
                [
                    "openssl",
                    "aes-256-cbc",
                    # "-d",
                    "-salt",
                    "-pbkdf2",
                    "-in",
                    in_path,
                    "-out",
                    out_path,
                    "-pass",
                    "pass:" + cls._password,
                ],
                check=True,
            )
        except Exception as ex:
            print(f"error decrypting file: {file_name} ex: {ex}")

        return True


## comando para encryptar los archivos (guardarlos en la carpeta extras)
# openssl aes-256-cbc -salt -pbkdf2 -in extras/cwallet.sso -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/ewallet.p12 -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/keystore.pem -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/ojdbc.properties -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/README -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/sqlnet.ora -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/tnsnames.ora -out temp/file.txt.enc -pass pass:holamundo
# openssl aes-256-cbc -salt -pbkdf2 -in extras/trustststoreB.ora -out temp/file.txt.enc -pass pass:holamundo
## decrypted
# openssl aes-256-cbc -d -salt -pbkdf2 -in app/extras/hola2.txt.enc -out app/temp/hola2.txt -pass pass:holamundo


# for i in $(ls enc); do echo "openssl aes-256-cbc -d -salt -pbkdf2 -in enc/$i -out dec/$i.enc -pass"; done
