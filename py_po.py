import subprocess
import psycopg2
from psycopg2 import OperationalError
import datetime

db_config = {
    'dbname': 'hunt',
    'user': 'biighunter',
    'password': '1122',
    'host': '146.190.26.15',
    'port': '5432',
}

backup_path = "/root/DateBase-demo/backup/"

current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M")
backup_filename = f'{formatted_datetime}_{db_config["dbname"]}_backup.sql'

def backup_database():
    try:
        connection = psycopg2.connect(**db_config)
        connection.autocommit = True
        print("Connected to the database")

        pg_dump_command = [
            '/usr/bin/pg_dump',
            f'--dbname=postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["dbname"]}',
            f'--file={backup_path}/{backup_filename}',
        ]

        subprocess.run(pg_dump_command, check=True)
        print("Backup completed successfully!")

    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
            print("Connection closed")

if __name__ == '__main__':
    backup_database()