import os
import subprocess


class AESCipher:
    """Class to mange AES Cipher."""

    _password = "holamundo" #sacar de los settings.password

    @classmethod
    def decrypt_all_files(cls, dir_in, dir_out):

        file_names = os.listdir(dir_in)
        for file_name in file_names:
            cls.decrypt_file(file_name, dir_in, dir_out)
        return True

    @classmethod
    def decrypt_file(cls, file_name, dir_in, dir_out):
        
        in_path = dir_in + file_name
        out_path = dir_out + file_name.replace('.enc', '')
        try:
            subprocess.run([
                'openssl', 'aes-256-cbc', '-d', '-salt', '-pbkdf2', '-in', in_path,
                '-out', out_path, '-pass', 'pass:' + cls._password
            ], check=True)
        except Exception as ex:
            print(f"error decrypting file: {file_name} ex: {ex}")

        return True

## comando para encryptar los archivos (guardarlos en la carpeta extras)
# openssl aes-256-cbc -salt -pbkdf2 -in file/file.txt -out file/file.txt.enc -pass pass:holamundo
## decrypted
# openssl aes-256-cbc -d -salt -pbkdf2 -in app/extras/hola2.txt.enc -out app/temp/hola2.txt -pass pass:holamundo
